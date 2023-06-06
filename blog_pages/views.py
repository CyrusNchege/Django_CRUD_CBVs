from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView,  UpdateView, DeleteView
from .models import Post

# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = "blog/list_detail.html"
    context_object_name = 'tasks'