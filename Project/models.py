from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=24)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Binder(models.Model):
    name = models.CharField(max_length=36)
    project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.SET_NULL)


class Resource(models.Model):
    url = models.URLField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Article(models.Model):
    """Table schema to store articles."""
    name = models.CharField(max_length=64)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    content = models.TextField()
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.name


class Author(models.Model):
    """Table schema to store auhtors."""
    name = models.CharField(max_length=64)
    slug = models.CharField(default='', max_length=64)

    def __str__(self):
        return '%s' % self.name