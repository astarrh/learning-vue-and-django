from django.forms import ModelForm

from .models import Project, Resource, Binder


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = ['name',]


class BinderForm(ModelForm):

    class Meta:
        model = Binder
        fields = ['name',]


class ResourceForm(ModelForm):

    class Meta:
        model = Resource
        fields = ['url',]


MODEL_FORMS = {
    "project": ProjectForm,
    "binder": BinderForm,
    "resource": ResourceForm
}
