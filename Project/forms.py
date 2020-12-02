from django.forms import ModelForm

from .models import Project, Resource, Task


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name',]


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'project']


class ResourceForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['url',]


MODEL_FORMS = {
    "project": ProjectForm,
    "task": TaskForm,
    "resource": ResourceForm
}
