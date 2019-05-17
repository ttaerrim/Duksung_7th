from django.db import models

# Create your models here.
class userdb(models.MOdel):
    id = models.CharField(max_length=30)
    upw = models.CharField(max_length=200, help_text='Enter password'
    th = models.IntegerField(blank=False, help_text='Enter th')
    email = models.Email_Field(blank=False)
    stu_id = models.IntegerField(blank=False, help_text='Enter student_id')
    staff = models.BooleanField(default=False)
    major = models.IntegerField(blank=False, help_text='Enter major')

    def __str__(self):
        return self.title
