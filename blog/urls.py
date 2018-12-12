from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:blog_id>/', views.blog_info, name='blog_info'),
    path('edit/', views.blog_edit, name='blog_add'),
    path('edit/<int:blog_id>/', views.blog_edit, name='blog_mod'),
    path('del/<int:blog_id>/', views.blog_del, name='blog_del'),
]
