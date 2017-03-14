# semo

[![Build Status](https://travis-ci.org/cosven/sevenmosquito.svg?branch=master)](https://travis-ci.org/cosven/sevenmosquito)
[![Documentation Status](https://readthedocs.org/projects/sevenmosquito/badge/?version=latest)](http://sevenmosquito.readthedocs.io/en/latest/?badge=latest)

### DEV Guide

```
# 创建 virtual env
python3 -m venv semo
source semo/bin/activate

# 安装依赖
pip install -r requirements.txt

# 启动依赖服务
# 1. mysql server (user:root, password:123456)
# 2. redis server

# 数据库表更新
./manage.py migrate

# 启动服务
./manage.py runserver

# 运行单元测试
./manage.py test

# 部署的主要过程
source /data/venv/semo/bin/activate
pip install -r requirements  # 如果有更新依赖
./manage.py migrate   # 如果有更新数据库
./manage.py collectstatic   # 如果有更新前端资源
supervisorctl restart semo  # 重启服务进程
```

### 主题调试参考

- [NexT-Pisces](http://notes.iissnan.com/)
- [NexT-Muse](https://javaclear.github.io/)
- [NexT-Mist](https://shevonwang.github.io/)
