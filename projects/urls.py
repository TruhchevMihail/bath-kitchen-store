from django.urls import path
from .views import (
    ProjectListView,
    ProjectCreateView,
    ProjectDetailView, ProjectUpdateView,
)

app_name = 'projects'

urlpatterns = [
    path('', ProjectListView.as_view(), name='projects_list'),
    path('create/', ProjectCreateView.as_view(), name='project_create'),
    path('<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('<slug:slug>/edit/', ProjectUpdateView.as_view(), name='project_edit'),
    path('<slug:slug>/delete/', ProjectDetailView.as_view(), name='project_delete'),
]
