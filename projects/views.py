from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from .models import ProjectPost
from .forms import ProjectPostCreateForm, ProjectPostUpdateForm


class ProjectBaseMixin:
    model = ProjectPost
    context_object_name = "project"
    paginate_by = 6

class ProjectListView(ProjectBaseMixin, ListView):
    template_name = "projects/projects_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        qs = super().get_queryset()
        section = self.request.GET.get("section")
        valid_sections = [ProjectPost.BATH, ProjectPost.KITCHEN]

        if section in valid_sections:
            return qs.filter(section=section)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["current_section"] = self.request.GET.get("section")
        return ctx


class ProjectDetailView(ProjectBaseMixin, DetailView):
    template_name = "projects/project_detail.html"


class ProjectCreateView(LoginRequiredMixin, ProjectBaseMixin, CreateView):
    form_class = ProjectPostCreateForm
    template_name = "projects/project_create.html"


class ProjectUpdateView(LoginRequiredMixin, ProjectBaseMixin, UpdateView):
    form_class = ProjectPostUpdateForm
    template_name = "projects/project_edit.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["slug"] = self.object.slug
        return initial


class ProjectDeleteView(LoginRequiredMixin, ProjectBaseMixin, DeleteView):
    template_name = "projects/project_delete.html"
    success_url = reverse_lazy("projects:projects_list")


