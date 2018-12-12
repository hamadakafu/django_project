from django.shortcuts import render, get_object_or_404, redirect

from .models import Blog
from .forms import BlogForm


def blog_list(request):
    all_blog = Blog.objects.all().order_by('id')
    return render(request, 'blog/blog_list.html', dict(all_blog=all_blog))


def blog_info(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_info.html', dict(blog=blog))


def blog_edit(request, blog_id=None):
    if blog_id:
        blog = get_object_or_404(Blog, pk=blog_id)
    else:
        blog = Blog()

    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog:blog_list')
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/blog_edit.html', dict(blog_id=blog_id, form=form))


def blog_del(request, blog_id):
    Blog.objects.filter(id=blog_id).delete()
    return redirect('blog:blog_list')
