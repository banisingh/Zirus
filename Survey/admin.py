from django.contrib import admin
from .models import Survey

# Register your models here.

@admin.register(Survey)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'created')