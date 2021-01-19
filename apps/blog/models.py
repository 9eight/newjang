from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"


class PostCategory(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=30)


class PostTags(models.Model):
    title = models.CharField(max_length=50)
    name = models.CharField(max_length=30)
