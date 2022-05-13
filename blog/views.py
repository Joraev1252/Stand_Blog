from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import BlogPostForm
from .models import BlogPostModel


def post_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST or None, request.FILES or None,)
        if form.is_valid():
            form.save()
            return redirect('general:blog_page')
    else:
        form = BlogPostForm()

    return render(request, 'blog_post.html', {'form': form})


def edit_blog(request, pk):
    try:
        blog = BlogPostModel.objects.get(id=pk)
    except:
        return HttpResponse("This blog not found!")

    if request.method == 'POST':
        form = BlogPostForm(data=request.POST or None, instance=blog)
        if form.is_valid():
            blog = form.save()
    form = BlogPostForm(instance=blog)
    context = {'form': form}
    return render(request, 'edit.html', context)





def delete_blog(request, pk):
    try:
        blog = BlogPostModel.objects.get(id=pk)
    except:
        return HttpResponse("This blog not found!")

    blog.delete()
    return redirect('general:blog_page')


def detail_view(request, pk):
    try:
        blog = BlogPostModel.objects.get(id=pk)


    except:
        return HttpResponse("This blog not found!")
    context = {
        'blog_detail': blog
    }
    return render(request, 'detail.html', context)
