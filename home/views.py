from django.shortcuts import render
from blogs.models import BlogPost
from gallery.models import Gallery


def home(request):
    data = request.session.get('data')
    context = {'blog_posts': BlogPost.objects.all(), 'allgallery_post': Gallery.objects.all()}
    if data:
        context['success'] = data['success']
    return render(request, "home/home.html", context)

def about(request):
    return render(request, "home/about.html")
