from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Navigation)
admin.site.register(models.Contents)
admin.site.register(models.Types)
admin.site.register(models.Blogs)
