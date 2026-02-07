from django.shortcuts import render

from django.shortcuts import render

def projects_list(request):
    return render(request, "projects/projects_list.html", {"posts": posts})

def project_detail(request, slug):
    return render(request, "projects/project_detail.html", {"slug": slug})
