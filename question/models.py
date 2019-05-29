from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(blank=True, upload_to="")


    def __Str__(self):
        return self.title

    def summary(self):
        return self.body[:50]

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
