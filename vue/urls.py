
from django.contrib import admin
from django.urls import path, include

# don't forget to import the app's view!
from Project import views as myapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('Project.urls', namespace="Project")),
    # paths for our app
    path('', myapp_views.frontend),
    path('triage/', myapp_views.TriageView.as_view(), name="triage"),
    path('article/<slug:slug>/', myapp_views.frontend),
    path('author/<slug:slug>/', myapp_views.frontend),
]