import json
from itertools import chain

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from .forms import MODEL_FORMS


def to_dict(instance):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields):
        data[f.name] = f.value_from_object(instance)
    for f in opts.many_to_many:
        data[f.name] = [i.id for i in f.value_from_object(instance)]
    return data


@ensure_csrf_cookie
def create_object(request):
    form_data = json.loads(request.body)
    model_class = form_data.pop('model')
    model_form = MODEL_FORMS[model_class](form_data)

    result = {'success': False}
    if model_form.is_valid():
        obj = model_form.save()
        result["success"] = True
        result['obj'] = json.dumps(to_dict(obj))
    else:
        result["errors"] = model_form.errors.as_json()

    return JsonResponse(result)
