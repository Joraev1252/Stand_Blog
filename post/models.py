from uuid import uuid4
from django.db import models
from django.urls import reverse


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = "news_archive/{filename}".format(
        filename='{}.{}'.format(uuid4().hex, ext))
    # file_path = f"news_archive/{f'{uuid4().hex}.{ext}'}"
    # file_path = f"news_archive/{uuid4().hex}.{ext}"
    return file_path


class PostModel(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = str(self.image.url)
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("general:blog_page", args=[str(self.id)])

