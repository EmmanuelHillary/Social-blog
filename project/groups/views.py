from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, RedirectView
from django.contrib import messages
from .models import Group, GroupMember

class CreateGroup(LoginRequiredMixin, CreateView):
    model = Group
    fields = ('name', 'description')
    context_object_name = 'groups'
    template_name = 'groups/form.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class SingleGroup(DetailView):
    model = Group
    context_object_name = 'groups'
    template_name = 'groups/detail.html'

class ListGroup(ListView):
    model = Group
    context_object_name = 'groups'
    template_name = 'groups/groups.html'

class JoinGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, ('Warning! already a member'))
        else:
            messages.success(self.request, 'You are now a member!')
        return super().get(request, *args, **kwargs)

class LeaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(user=self.request.user, group__slug=self.kwargs.get('slug')).get()

        except GroupMember.DoesNotExist:
            messages.warning(self.request, ('Sorry, you are not in this group!'))
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')
        return super().get(request, *args, **kwargs)
