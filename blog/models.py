from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Tag(models.Model):
    """博客分类"""
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tag_name


# class Category(models.Model):
#     name = models.CharField(max_length=30, verbose_name='分类名称')
#     index = models.IntegerField(default=999, verbose_name='分类的排序')
#
#     class Meta:
#         verbose_name = '分类'
#         verbose_name_plural = verbose_name
#         ordering = ['index', 'id']
#
#     def __str__(self):
#         return self.name


class Blog(models.Model):
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)  # 一对一外键，关联作者模型
    tags = models.ManyToManyField(Tag, blank=True)  # 多对多字段，绑定下面的Tag模型
    content = models.TextField()  # Text长文本字段，可以写很多内容
    publish_time = models.DateTimeField(auto_now_add=True)  # 日期，新增自动写入
    update_time = models.DateTimeField(auto_now=True)  # 日期，修改自动更新

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.caption


