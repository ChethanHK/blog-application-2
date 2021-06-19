from . import views
from django.urls import path

urlpatterns = [
  path('', views.PostList.as_view(), name="home"),
  path('<slug:slug>/', views.PostList.as_view(), name="post_detail"),
  path('<int:post_id>/share/', views.DetailView.post_share, name='post_share'),
]