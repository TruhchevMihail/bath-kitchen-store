from django.shortcuts import render

from django.shortcuts import render

def projects_list(request):
    #todo: replace with real queries after models exist
    posts = [
        {"slug": "modern-bathroom", "title": "Modern Bathroom", "excerpt": "Modern bathroom design"},
    ]
    return render(request, "projects/projects_list.html", {"posts": posts})

def project_detail(request, slug):
    return render(request, "projects/project_detail.html", {"slug": slug})
