 from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class postlist(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = "all_post_l"
class postdetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = "all_post_d"
class postnew(CreateView):
    model = Post
    template_name = "new_post.html"
    fields = "__all__"

class editpost(UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ['title','body']

class deletepost(DeleteView):
    model = Post
    template_name= "delete_post.html"
    success_url = reverse_lazy('home')