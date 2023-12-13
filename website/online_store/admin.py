from django.contrib import admin

from .models import Drawing


class DrawingAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'published', 'image_tag')
    list_display_links = ('title', 'description')
    search_fields = ('title', 'price')
    readonly_fields = ('image_tag',)


admin.site.register(Drawing, DrawingAdmin)
