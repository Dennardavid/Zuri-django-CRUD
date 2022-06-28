
from django.views.generic.edit import CreateView
from .models import Post
from django.urls import reverse_lazy

class PostListView(CreateView):
    model = Post
    fields = "__all__"
    
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class  PostDetailView(CreateView):
    model = Post
    fields = "__all__"
    
class PostUpdateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDeleteView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")
   


