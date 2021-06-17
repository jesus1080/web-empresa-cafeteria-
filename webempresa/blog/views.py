from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts':posts})

def category(request, category_id):
    #get_object_or_404 para controlar el error al pasar un id de categoria que no existe
    category = get_object_or_404(Category, id=category_id)
    return render(request, "blog/category.html", {'category':category})