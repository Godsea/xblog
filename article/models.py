from django.db import models

# Create your models here.
from mdeditor.fields import MDTextField


# 导航
class Navigation(models.Model):
    name = models.CharField(max_length=50,verbose_name='导航应用')

    class Meta():
        db_table = 'navigation'

    def __str__(self):
        return self.name


# 项目
class Contents(models.Model):
    name = models.CharField(max_length=50,verbose_name='项目名称')
    nav = models.ForeignKey(Navigation,null=True,blank=True,verbose_name='导航应用',on_delete=models.CASCADE)


    class Meta():
        db_table = 'contents'

    def __str__(self):
        return self.name


# 二级类别
class Types(models.Model):
    name = models.CharField(max_length=50,verbose_name='目录名称')
    nav = models.ForeignKey(Navigation,null=True,blank=True,verbose_name='导航应用',on_delete=models.CASCADE)
    con = models.ForeignKey(Contents,null=True,blank=True,verbose_name='项目',on_delete=models.CASCADE)
    class Meta():
        db_table = 'types'

    def __str__(self):
        return self.name


# 文章
class Blogs(models.Model):
    nav = models.ForeignKey(Navigation,null=True,blank=True,verbose_name='导航应用',on_delete=models.CASCADE)
    con = models.ForeignKey(Contents,null=True,blank=True,verbose_name='项目',on_delete=models.CASCADE)
    ty = models.ForeignKey(Types,null=True,blank=True,verbose_name='目录',on_delete=models.CASCADE)
    name = models.CharField(max_length=30,verbose_name='索引名称')
    content = MDTextField()

    class Meta():
        db_table = 'blogs'

    def __str__(self):
        return self.name

