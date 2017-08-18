from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Category, Post, Tag, User
from comments.forms import CommentForm
from django.views.generic import ListView
from django.views.generic import DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import markdown

# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-creat_time')
    # print("blog index in ")
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/index.html', context={'post_list': posts})


# def detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/detail.html', context={'post': post})

# detail with markdown
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
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


def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=tag).order_by('-creat_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = 'please input the search keyword'
        return render(request, 'blog/index.html', {'error_msg': error_msg})
    post_list = Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'error_msg': error_msg, 'post_list': post_list})


