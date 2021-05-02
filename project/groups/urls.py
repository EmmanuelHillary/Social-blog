from django.urls import path
from .views import ListGroup, SingleGroup, CreateGroup, LeaveGroup, JoinGroup

app_name = 'groups'

urlpatterns = [
    path('', ListGroup.as_view(), name='all'),
    path('new/', CreateGroup.as_view(), name='create'),
    path('posts/in/<slug:slug>/', SingleGroup.as_view(), name='single'),
    path('leave/<slug:slug>/', LeaveGroup.as_view(), name='leave'),
    path('join/<slug:slug>/', JoinGroup.as_view(), name='join'),


]
