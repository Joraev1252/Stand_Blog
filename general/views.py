from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import BlogPostModel
from post.models import PostModel


@login_required
def main_home(request):
    context = {}
    return render(request, 'main/home.html')


@login_required
def about(request):
    context = {}
    return render(request, 'main/about.html')


@login_required
def blog(request):
    blogs = BlogPostModel.objects.all()
    context = {
        'blog_in_template': blogs  # "blog_in_template" we use for logical operations in html files
    }
    return render(request, 'main/blog.html', context)


@login_required
def detail(request):
    post = PostModel.objects.all()
    context = {
        'post_template': post
    }
    return render(request, 'main/details.html', context)


@login_required
def contact(request):
    context = {}
    return render(request, 'main/contact.html')


