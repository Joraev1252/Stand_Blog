from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import PostForm
from .models import PostModel


def post_blog_views(request):
    if request.method == 'POST':
        form = PostForm(request.POST or None, request.FILES or None,)
        if form.is_valid():
            form.save()
            return redirect('general:blog_detail')
    else:
        form = PostForm()

    return render(request, 'blog_post.html', {'form': form})


def edit_blog(request, pk):
    try:
        blog = PostModel.objects.get(id=pk)
    except:
        return HttpResponse("This blog not found!")

    if request.method == 'POST':
        form = PostForm(data=request.POST or None, instance=blog)
        if form.is_valid():
            blog = form.save()
    form = PostForm(instance=blog)
    context = {'form': form}
    return render(request, 'edit.html', context)








def delete_blog(request, pk):
    try:
        blog = PostModel.objects.get(id=pk)
    except:
        return HttpResponse("This blog not found!")

    blog.delete()
    return redirect('general:blog_detail')


def detail_view(request, pk):
    try:
        blogs = PostModel.objects.get(id=pk)
    except:
        return HttpResponse("This blog not found!")
    context = {
        'blog_post': blogs
    }
    return render(request, 'detail_post.html', context)
