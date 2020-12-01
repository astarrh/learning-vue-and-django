import json

from django.views.generic import TemplateView

from django.shortcuts import render

from .models import Project


class TriageView(TemplateView):
    template_name = "html/template.html"

    def projects(self):
        return Project.objects.all()
