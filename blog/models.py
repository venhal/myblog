from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#分类
class Category(models.Model):
    name = models.CharField(max_length=100)
#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)
#文章
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)

    # 文章正文，TextField可以存储更大文本
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型。
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以没有文章摘要，但默认情况下 CharField 要求我们必须存入数据，否则就会报错。
    excerpt = models.CharField(max_length=200, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)