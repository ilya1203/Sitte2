from django.contrib import admin


from .models import Nns
from .models import Rubric

class NnsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'published', 'rubric', 'photo')
    list_display_links = ('title', 'content', 'rubric')
    search_fields = ('title', 'content')

admin.site.register(Nns, NnsAdmin)
admin.site.register(Rubric)
