from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=24)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=24)
    url = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='resources')


class Task(models.Model):
    name = models.CharField(max_length=36)
    high_priority = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='tasks')
