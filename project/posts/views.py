from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views.generic import *
from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.contrib.auth.models import User as Us

from .models import Post
from posts import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class PostList(SelectRelatedMixin, ListView):
    model = Post
    select_related = ('user', 'group')
    template_name = 'posts/posts.html'
    context_object_name = 'posts'

class UserPosts(ListView):
    model = Post
    template_name = 'posts/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context

class PostDetail(SelectRelatedMixin, DetailView):
    model = Post
    select_related = ('user', 'group')
    template_name = 'posts/detail.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin, SelectRelatedMixin, CreateView):
    model = Post
    fields = ('message', 'group')
    context_object_name = 'posts'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin, SelectRelatedMixin, DeleteView):
    model = Post
    select_related = ('user', 'group')
    template_name = 'posts/delete.html'
    context_object_name = 'posts'

    def get_success_url(self, **kwargs):
        return reverse_lazy('posts:for_user', kwargs={'username': self.request.user.username})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
