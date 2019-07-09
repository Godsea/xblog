### xblog
---
#### 1.项目描述
> xblog博客系统1.0版

#### 2.0安装配置

环境需求：
> - python3.*以上
> - django2.*以上

安装程序：

```
git clone https://github.com/Godsea/xblog.git
```

python3环境下安装依赖包：
```
pip install django-mdeditor
pip install markdown
pip install mysqlclient
```

完成安装：
```
python manage.py migrate
python manage.py makemigrations

```