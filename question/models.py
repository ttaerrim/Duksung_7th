from django.db import models
from django import forms
from django.urls import reverse

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    #board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name='comments')
    #author
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_edit_url(self):
        return reverse('comment_edit', args=[self.board.pk, self.pk])



   