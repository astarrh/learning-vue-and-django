from django.urls import path

from Project import actions

app_name = "Project"

urlpatterns = [
    path('create_object/', actions.create_object, name='create_object')
]