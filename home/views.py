from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Count
from django.urls import reverse_lazy

from .models import Post,Category,User
from .forms import PostForm, CommentForm, CategoryForm
# Create your views here.
def homepage(request):
    return render(request,'home/base.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'home/registration/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('logout')
    else:
        form = UserCreationForm()
    return render(request, 'home/registration/register.html', {'form': form})


class PostListView(ListView):
    model = Post
    template_name = 'home/posts/post_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.select_related('author').annotate(comment_count=Count('comments'))

class PostDetailView(DetailView):
    model = Post
    template_name = 'home/posts/post_detail.html'
    context_object_name = 'post'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['categories'] = self.object.categories.all()
        context['comment_form'] = CommentForm()
        return context
    
@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'home/posts/post_form.html'
    success_url = reverse_lazy('post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    return redirect('post_detail', pk=pk)

@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'home/posts/category_form.html'
    success_url = reverse_lazy('category_posts') 

class UserPostCountView(ListView):
    model = User
    template_name = 'home/posts/user_post_count.html'
    context_object_name = 'users'
    
    def get_queryset(self):
        return User.objects.annotate(post_count=Count('posts')) # create new collection of Users with new temp attribute 'post_count' on every record ('row')
                # SELECT * FROM Users WHERE Post = user.name
                # SELECT * FROM Users JOIN Posts ON Users.name = Post.author

class MostCommentedPostsView(ListView):
    model = Post
    template_name = 'home/posts/most_commented_posts.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.annotate(comment_count=Count('comments')).order_by('-comment_count')[:5]

class PostsWithoutCommentsView(ListView):
    model = Post
    template_name = 'home/posts/posts_without_comments.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(comments__isnull=True)

class CategoryPostListView(ListView):
    model = Category
    template_name = 'home/posts/category_posts.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.prefetch_related('posts')