from django.urls import path
from .views import login_view, logout_view, register_view,homepage,PostListView,PostDetailView,PostCreateView,add_comment,CategoryCreateView,UserPostCountView,MostCommentedPostsView,PostsWithoutCommentsView,CategoryPostListView

urlpatterns=[
    path("",homepage, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('user-posts/', UserPostCountView.as_view(), name='user_post_count'),
    path('most-commented/', MostCommentedPostsView.as_view(), name='most_commented_posts'),
    path('no-comments/', PostsWithoutCommentsView.as_view(), name='posts_without_comments'),
    path('categories/', CategoryPostListView.as_view(), name='category_posts'),
]