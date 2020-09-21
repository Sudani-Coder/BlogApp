from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='home'),
    path('user/<str:username>', views.UserPostListView.as_view(), name="UserPosts"),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('post/new/', views.PostCreateView.as_view(), name='PostCreate'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='PostUpdate'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='PostDelete'),
    path('about/', views.about, name='about'),
]
