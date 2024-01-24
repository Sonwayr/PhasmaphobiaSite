from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *


# Register your models here.
@admin.register(Ghost)
class GhostAdmin(admin.ModelAdmin):
    """Модель призрака в админ-панеле"""
    list_display = ('id', 'name', 'slug', 'properties', 'display_evidences')
    list_display_links = ('slug', 'name')
    list_per_page = 10
    search_fields = ('name',)

    def display_evidences(self, obj):
        """Отображение улик и ссылки на них"""
        links = [f'<a href="/admin/main/evidence/{evidence.pk}/change/">{evidence}</a>'
                 for evidence in obj.evidences.all()]
        return format_html(', '.join(links))

    display_evidences.short_description = 'Улики'


@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    """Модель улики в админ-панеле"""
    list_display = ('id', 'name', 'slug', 'properties', 'display_ghosts')
    list_display_links = ('slug', 'name')
    search_fields = ('name',)

    def display_ghosts(self, obj):
        """Отображение призраков и ссылки на них"""
        ghosts_links = [f'<a href="/admin/main/ghost/{ghost.pk}/change/">{ghost}</a>'
                        for ghost in obj.ghosts.all()]
        return format_html(', '.join(ghosts_links))

    display_ghosts.short_description = 'Призраки'
