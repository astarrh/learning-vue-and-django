import json
from itertools import chain

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from .forms import MODEL_FORMS
from .models import Project, Task


def model_to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


# @ensure_csrf_cookie
def create_object(request):
    form_data = json.loads(request.body)
    model_class = form_data.pop('model')
    model_form = MODEL_FORMS[model_class](form_data)

    result = {'success': False}
    if model_form.is_valid():
        obj = model_form.save()
        result["success"] = True
        result['obj'] = json.dumps(model_to_dict(obj))
    else:
        result["errors"] = model_form.errors.as_json()

    return JsonResponse(result)


def get_resources(request):
    form_data = json.loads(request.body)
    result = {'success': False}
    project = Project.objects.filter(id=form_data.get('obj')).first()
    if project:
        resource_urls = project.resources.all().values_list('url')
        if resource_urls:
            result['success'] = True
            result['payload'] = resource_urls
        else:
            result['payload'] = "No Resources have been added for this project"
    else:
        result['payload'] = "Project Not Found."
    return JsonResponse(result)


def complete_task(request):
    form_data = json.loads(request.body)
    task = Task.objects.filter(id=form_data.get('obj')).first()
    task.completed = True if task.completed is False else True
    task.save()
    result = {'success': True}
    return JsonResponse(result)
