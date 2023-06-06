from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogListView.as_view(), name= 'blog_list'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name= "blog_detail"),
    path('create/', views.BlogCreateView.as_view(), name='blog_create')
]