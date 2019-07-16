from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return "%s" % (self.name)

class Post(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=30, default="Somewhere Mysterious")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    thumb = models.ImageField(default='default.png')
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return "%s" % (self.title)

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
