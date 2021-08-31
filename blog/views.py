from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post
# def detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     context = { 'object':post, 'post':post}
#     return render(request, 'blog/detail.html', {'post':post}, context) ############ 수정하는 중에 넘어감


# def index(request):
#     posts = Post.objects.all()
        # object_list = Post.objects.all() -- class PostList가 사용대면 윗 줄 대신이용...?
#     context = {'posts' : posts}
        # context = {'object_list':object_list} -- class PostList가 사용대면 윗 줄 대신이용...?
#     return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/detail.html', {'post':post})