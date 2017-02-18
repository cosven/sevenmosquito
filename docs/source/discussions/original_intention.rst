original intention
==================

2017-2-4 by cosven.

大概是这样的目标
----------------

这是一个网站，一个用来写 **技术博客** 的地方。幸运的话，希望它能成为一个交流技术的地方。
再 **幸运** 一点的话，它也会肩负 **记载生活** 的任务。（希冀还是要有的，万一实现了呢？）

所以目前这个网站大概需要三个大的功能：博客 **编辑** 、 **展示** 、 **评论**  。

诶，有几个问题？
----------------

写技术博客？
^^^^^^^^^^^^

为啥不用 Github Pages? 不知道啊，宝宝不喜欢。
为啥不用 wordpress? 不知道啊，宝宝也不太喜欢。

其实嘛：

1. Github Pages 它是静态的

   - 或许不是每个人都喜欢这个方式...
   - 或许仍然有点麻烦。本地编辑 -> push -> 博客展示

2. wordpress 其实也没什么不好的。
3. 宝宝还年轻...（或许这很关键）
4. 并不能实现记录生活的伟大目标...（这个也很关键喽）

打算怎么做哩？
--------------

自己做喽...先搭个后台

| 会 java 嘛？不会，没学过
| 会 nodejs 嘛？你以为我是全栈...
| 会 php 嘛？膜拜
| 会 python 嘛？会一点。那用 flask，不开心啊。那就用 django 把

前端呢？深似海。弃疗。找个小伙伴帮帮忙？好像没有不是很适合吧...

::

    A: 你听说过 material design ？
    B: 你是说 ``materializecss`` 还是 ``material-design-lite`` 还是
    A: 好吧，你听说过 Bootstrap ？
    B: 臣妾不想要这么好用的东西，臣妾还年轻呢
    A: 好吧，你听说过 hexo 么？
    B: Github Pages ？
    A: 那你应该听说过 next 么？
    B: 一个主题？据说颜值很高诶
    A: 那你听说过 swig 么？
    B: 深似海...
    A: Swig is an awesome, Django/Jinja-like template engine for node.js.
    B: 诶，django/jinja-like ? 可以

所以就 django + next 把，（脑袋被拍碎了）

mysql vs postgres vs mongodb ？宝宝还是继续研究研究 mysql 把

nginx + supervisor + gunicorn ? 差不多将就着用吧

恩，所以总的来说就是：nginx + gunicorn + django + mysql + hexo-theme-next

细节部分， 拆拆模块？
^^^^^^^^^^^^^^^^^^^^^

1. 博客展示：前端套用 hexo-theme-next 的模板
2. 博客编辑页面：需要自己另外找模板弄一个页面。或者基于现在的模板，自己写。
3. 博客评论：之后接入 duoshuo, disqus 这样现成的系统。（大概只需要引入一个 js 就够了？还需要小小的调研一发。）有需要的话，也可以自己开发前后端。

博客编辑的话，内容以 markdown 的形式保存。

网站特殊性？
-----------

需要支持多域名
^^^^^^^^^^^^^^

描述：我们希望用户访问 a.com 的时候得到的内容是 a 的相关信息。用户访问 b.com 的时候，得到的内容是 b 相关的信息。但是这两个域名是共用一个后台的。

还要考虑以后子域名的情况：比如 blog.a.com/blog.b.com, happy.a.com/life.b.com。



大概的架构图？
^^^^^^^^^^^^^^

图形展示？

.. graphviz::

   digraph {
     user_visit -> nginx
     nginx -> gunicorn
     supervisor -> gunicorn [label="管理服务进程"]
     gunicorn -> webserver
     webserver -> mysql
     webserver -> redis [style=dashed, label="缓存"]
     webserver -> offline_task [style=dashed]
     webserver -> image_service [style=dashed] [label="提供图片存储"]
     mysql -> backup [style=dashed]

     user_visit [label="yannnli.me, cosven.me, *.*.*"]
     webserver [label="django + next 模板"]
     image_service [label="图片服务（或许可以使用 qiniu 等）"]
     nginx [label="NGINX"]
     redis [label="Redis 后期考虑到性能或者一些缓存功能，很可能会用到"]
     offline_task [label="一年活动可视化？特征提取啥的？"]
     backup [label="数据备份"]
   }
