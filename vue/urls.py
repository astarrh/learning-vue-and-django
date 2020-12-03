
from django.contrib import admin
from django.urls import path, include

# don't forget to import the app's view!
from Project import views as myapp_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('Project.urls', namespace="Project")),
    path('', myapp_views.HomeView.as_view(), name="home"),
]