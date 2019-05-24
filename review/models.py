from django.db import models

# Create your models here.
class Review(models.Model):
    who = models.CharField(max_length=200)
    #라디오 버튼 처리?? category
    role = models.CharField(max_length=200)
    write = models.TextField()

    def __str__(self):
        return self.who