import json

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse

from .forms import MODEL_FORMS


@ensure_csrf_cookie
def create_object(request):
    form_data = json.loads(request.body)
    model_class = form_data.pop('model')
    model_form = MODEL_FORMS[model_class](form_data)

    result = {'success': False}
    if model_form.is_valid():
        model_form.save()
        result["success"] = True
    else:
        result["errors"] = model_form.errors.as_json()

    return JsonResponse(result)
