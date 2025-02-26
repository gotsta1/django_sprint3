from django.urls import path
from .views import HomePage, PostDetail, CategoryPosts

app_name = 'blog'

urlpatterns = [
    path('', HomePage.as_view(), name='index'),
    path('posts/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('category/<slug:pk>', CategoryPosts.as_view(), name='category_posts')
]
