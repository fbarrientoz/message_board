from django.views.generic import ListView
from django.shortcuts import render
from .models import Post

# Create your views here.
class HomePageView(ListView):
    """
    docstring
    """
    model = Post
    template_name = 'home.html'

    content_object_name = "all_post_list"