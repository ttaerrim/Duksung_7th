from django.db import models
from django import forms
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True,null=True, upload_to="")
    hits = models.PositiveIntegerField(default = 0) # 조회수
    writer = models.CharField(max_length=100, blank=True) # 작성자
    solved = models.BooleanField(default=False) # 해결 여부
    like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
    blank=True, related_name='like_user_set', through='Like')
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]


    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
    @property
    def update_counter(self):
        self.hits = self.hits + 1
        self.save()
        return ""

class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Board, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('user', 'post'))

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    #board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    #author
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_edit_url(self):
        return reverse('comment_edit', args=[self.board.pk, self.pk])

