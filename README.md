# semo

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
```

### 主题调试参考

- [NexT-Pisces](http://notes.iissnan.com/)
- [NexT-Muse](https://javaclear.github.io/)
- [NexT-Mist](https://shevonwang.github.io/)
