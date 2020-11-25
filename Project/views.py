from django.views.generic import TemplateView

from django.shortcuts import render

from .models import Article, Author, Project, Resource, Binder

def frontend(request):
    """Vue.js will take care of everything else."""
    articles = Article.objects.all()
    authors = Author.objects.all()

    data = {
        'articles': articles,
        'authors': authors,
    }

    return render(request, 'html/template.html', data)


class TriageView(TemplateView):
    template_name = "html/triage.html"

    def projects(self):
        return Project.objects.all()
