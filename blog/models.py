from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title      = models.CharField(max_length=100)   # 제목
    content    = models.TextField()                 # 본문
    head_image = models.ImageField(upload_to='blog/%Y/%m/%d/', blank=True)   # 첨부이미지
    created    = models.DateTimeField(blank=True)   # 글쓴 시점
    author     = models.ForeignKey(User, models.CASCADE)   # 글쓴이

    def __str__(self):
        return "{}::{}".format(self.title, self.author)
