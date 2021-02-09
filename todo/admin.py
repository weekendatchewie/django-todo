from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)      # Permet d'afficher la date de création dans l'admin


admin.site.register(Todo, TodoAdmin)
