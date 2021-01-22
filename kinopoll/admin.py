from django.contrib import admin

from kinopoll import models

# Register your models here.
admin.site.register(models.Poll)
admin.site.register(models.Question)
admin.site.register(models.Option)