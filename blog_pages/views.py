from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView,  UpdateView, DeleteView
from .models import Post
from .forms import PostCreateForm
from django.urls  import reverse_lazy

# Create your views here.
class BlogListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "blog/list.html"
    context_object_name = 'blogs'

class BlogDetailView(DetailView):
    queryset = Post.objects.all()
    template_name = "blog/task_detail.html"
    context_object_name = 'blogs'
   
class BlogCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "blog/task_create.html"
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = "blog/task_update.html"
    success_url= reverse_lazy('blog:blog_list')

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/task_delete.html'
    success_url= reverse_lazy('blog:blog_list')