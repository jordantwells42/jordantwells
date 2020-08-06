from django.shortcuts import render
from .models import Post

# Create your views here.
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
        "title": "Blog"
    }
    return render(request, "blog/blog_index.html", context)

def post_detail(request, pk):
    post = Post.objects.get(pk = pk)

    context = {
        "post": post,
        "title": "Blog"
    }


    return render(request, "blog/blog_post.html", context)