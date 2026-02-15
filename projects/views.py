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
            qs = qs.filter(section=section)

        q = (self.request.GET.get('q') or '').strip()
        if q:
            if len(q) < 2:
                qs = qs.none()
            else:
                qs = qs.filter(title__icontains=q)

        sort = self.request.GET.get('sort', '-created_at')
        valid_sorts = {
            'newest': '-created_at',
            'oldest': 'created_at',
            'title': 'title',
            '-title': '-title',
        }
        db_sort = valid_sorts.get(sort, '-created_at')
        return qs.order_by(db_sort)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["current_section"] = self.request.GET.get("section")
        ctx['current_sort'] = self.request.GET.get('sort', 'newest')
        return ctx


class ProjectDetailView(ProjectBaseMixin, DetailView):
    template_name = "projects/project_detail.html"


class ProjectCreateView(ProjectBaseMixin, CreateView):
    form_class = ProjectPostCreateForm
    template_name = "projects/project_create.html"


class ProjectUpdateView(ProjectBaseMixin, UpdateView):
    form_class = ProjectPostUpdateForm
    template_name = "projects/project_edit.html"

    def get_initial(self):
        initial = super().get_initial()
        initial["slug"] = self.object.slug
        return initial


class ProjectDeleteView(ProjectBaseMixin, DeleteView):
    template_name = "projects/project_delete.html"
    success_url = reverse_lazy("projects:projects_list")

