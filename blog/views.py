from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Category, Post, Tag, User
from comments.forms import CommentForm
import markdown

# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-creat_time')
    # print("blog index in ")
    return render(request, 'blog/index.html', context={'post_list': post_list})


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/detail.html', context={'post': post})

# detail with markdown
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list
    }

    # return render(request, 'blog/detail.html', context={'post': post})
    return render(request, 'blog/detail.html', context=context)


def archives(request, year, month):
    post_list = Post.objects.filter(creat_time__year=year, creat_time__month=month).order_by('-creat_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-creat_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


