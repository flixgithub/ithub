# Create your views here.
# -*- coding:utf8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm
import markdown


def post_comment(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # 利用表单数据生成一个Comment类型的model实例（commit=False 表示表单数据先不保存到数据库）
            comment = form.save(commit=False)
            # 创建一对多的关系，一个帖子对应多个评论
            comment.post = post
            # 将评论的数据保存到数据库
            comment.save()
            # 重定向到post详情页面，会自动调用post.get_absolute_url()方法，获得跳转路由信息
            return redirect(post)
        else:
            # 相当于comment_list = Comment.objects.filter(post=post), 即根据post来过滤该post下的评论
            comment_list = post.comment_set.all()
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blog/detail.html', context=context)
    return redirect(post)