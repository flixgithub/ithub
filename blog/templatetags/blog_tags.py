# -*- coding:utf8 -*-
from django import template  # 引入模板的类
from django.db.models.aggregates import Count
from django.db.models import Count
from ..models import Post, Category, Tag


register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-creat_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.datetimes('creat_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)






