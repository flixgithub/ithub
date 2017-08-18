from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.html import strip_tags
import markdown


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    creat_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    outline = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.pk])

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        if not self.outline:
            md = markdown.Markdown(extensions=[
                    'markdown.extensions.extra',
                    'markdown.extensions.codehilite',
                ])
            self.outline = strip_tags(md.convert(self.body))[:54]
        super(Post, self).save()









