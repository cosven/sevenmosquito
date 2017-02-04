# feeluown 阶段性总结即分享

主要介绍：feeluown 的整个结构，以及一些(GUI)开发的感悟
## 项目定位

Linux 上支持虾米，网易云，QQ三大平台的音乐播放器
### 背景
- 当时 Linux 的播放器基本不支持在线音乐播放。大部分音乐播放器只支持：last.fm 等音乐平台。
- 存在一些第三方音乐播放器：类似 [deepin music player](https://github.com/linuxdeepin/deepin-music)，支持百度音乐，
  [kuwo](https://github.com/LiuLang/kwplayer) 酷我音乐，
  [虾米电台](http://forum.ubuntu.org.cn/viewtopic.php?f=74&t=380947)，功能简陋把
- 当时网易云音乐正在占据大部分市场
- 个人用着 Linux，闲着无聊，觉得爬爬网站貌似还挺有趣（这个是主要原因，目测）
### 项目迭代的一些过程
- [第一版](https://www.oschina.net/code/snippet_1244912_46250)
  ![](https://static.oschina.net/uploads/code/201503/13025515_Siqt.jpg)
- 第二版
  ![第二版](https://static.oschina.net/uploads/code/201503/30075430_zmtx.png)
- 中间一个成熟的版本
  ![](https://bbs.deepin.org/data/attachment/forum/201511/10/222309uoxxo25xw515zpxt.png)
- 发版截图
  ![发布的一些截图](http://7xnn7w.com1.z0.glb.clouddn.com/feeluown-history.jpeg)
- ...
- 现在...
  ![](https://cloud.githubusercontent.com/assets/4962134/17672685/235ae556-6350-11e6-98c6-1f18051e5da1.png)
### GUI 软件开发概述

流行的 GUI 库：Linux 上主要是 GTK，Qt。Windows 上 MFC，Mac OSX cocoa。
跨平台：gtk, wxWidgets, Qt。
GPU 加速的 gui 库：Gac (vczh 貌似在知乎上也很有名的)

Qt 接口比较好用，wxWidgets 比较丑，GTK 官方后来才正式支持多平台
许多嵌入式系统界面也会采用 qt 。

Qt 出了个 QML 也能开发安卓软件。不过 QML 对 PC 平台支持不是特别完善。
(Qt 本省不仅仅提供了 GUI 相关的功能，还有一些网络请求，OpenGL 的封装等)

最新的一些做 GUI 的工具：[Electron](https://github.com/electron/electron), [nw.js](https://github.com/nwjs/nw.js/)。
据说前者优于后者，且有成熟应用。
#### pyqt5 最简单的 demo
- http://zetcode.com/gui/pyqt5/firstprograms/
- `python3 /tmp/gui.py`
1. 定义一个布局（有网格布局，水平Box布局等）
2. 往布局里面塞一堆控件（和 HTML 很像，button，label等）
3. 控件上绑定各种事件（比如点击事件，鼠标 hover 事件）
##### 关于 GUI，可能会有这些些问题：
1. 进度条怎么做的？
2. 透明、阴影等特效怎么做？
3. 顶部 panel 的图标怎么弄？
4. 怎样显示系统通知？
5. 怎样置顶？
6. 音乐播放器怎样控制？
##### 关于音乐播放器，有这些一些概念：
1. [MPRIS Media Player Remote Interfacing Specification](https://specifications.freedesktop.org/mpris-spec/latest/)
2. [MPD Music Player Daemon](https://www.musicpd.org/)
##### 关于 Linux, 有个 D-BUS 的东西和开发联系比较紧密

感觉和安卓，IOS开发应该也很类似

很久很久以前写安卓 2.3 的时候：它也是一个 layout.xml 文件加上各种事件响应 activity

和游戏 UI 开发也很类似
### FeelUOwn 项目'架构'

目前：

```
widget+widget+...+widgets -> UI
UI -> app (控制中心，相当于一个 mixins ?)

app: ui(.status_line .progress_bar)
     player
     theme_manager
     request_manager -> 统一网络错误提示消息
     plugin
     hotkey
     ...

# 为了兼容多个音乐平台
model: BaseModel: BaseSongModel
                  BaseAlbumModel
                  ...

# 插件模块
## 以一个 python package 的形式扔在一个 plugins 文件夹中，程序自动扫
实现几个字段和函数
## 热插拔...

__version__
__feeluown_version__
__alias__
__desc__
def enable(app)
def disable(app)

# 远程控制模块
目前实现了一个 udp server：感觉有问题。

## 存在的一些问题：
1. 接口不能很好的抽象： app.
2. app 就像一个大的 mixins，感觉迟早会有问题
```

中间也尝试过：

```
# 以前想通过 webview 和 d3.js 等前端技术做一些炫酷的效果，但是感觉会有性能问题
webview + native + Controller (但是有性能问题，加载时间稍长，表现为内存占用大，CSS动画不流畅)
```

最新架构预想：

```
player + 数据 model 作为一个 daemon

提供 qt-based GUI
提供 vim-based GUI
```
### GUI 开发的不同的点（相对于 Web 开发）
###### Signal 机制
###### GUI 中，UI 逻辑会占据大部分代码。
###### GUI 界面渲染的过程

一个 widget，它会定时刷新自己的页面（每次都会调用一个叫做 `paintEvent` 的函数）。
所以可以通过重写这个函数来自定义界面长相，也可以通过类似 css 的东西来定义界面样式
###### GUI 软件发布之后不能在服务端更新它。需要玩家主动升级
###### 测试相对较难

之前本来有集成测试的（目前没测试...）
### 项目开发过程中主要解决的几个技术问题
1. UI 美化 -> 重写绘图函数
2. 网络操作 -> quamash(asyncio+qt event-loop)
3. 插件机制 -> 规范接口
4. 主题更换机制 -> 统一接口
5. 音乐资源获取 -> 抓包
6. 远程控制 -> 目前有个非常简单的 udp server，感觉需要 RPC ?
7. 歌曲缓存(想做到像视频缓存那样) -> 但是目前没解决...(播放器核心不是自己写的，也没看它提供什么接口)
### neovim 插件开发

vim 插件开发的实质：就是把我们平常按键的顺序写到代码中，进行一些错误判断，然后绑定各种 key。

