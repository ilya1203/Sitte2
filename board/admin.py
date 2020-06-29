from django.contrib import admin


from .models import Comments

class CcontAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Text', 'published')
    list_display_links = ('Name', 'Text', 'published')
    search_fields = ('Name', 'Text', 'published')

admin.site.register(Comments, CcontAdmin)
# Register your models here.
