from django.db import models

# Create your models here.

class apply(models.Model):
    name = models.CharField(max_length=6)
    major = models.CharField
    student_id = models.IntegerField
    email = models.EmailField
    phone = models.IntegerField
    body = models.TextField
    file = models.FileField
    isFinal = models.CharField
