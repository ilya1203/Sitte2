from django.contrib import admin

from .models import Cont
from .models import Rubric

class ContAdmin(admin.ModelAdmin):
    list_display = ('title', 'textContent', 'published')
    list_display_links = ('title', 'textContent')
    search_fields = ('title', 'textContent')

admin.site.register(Cont, ContAdmin)
admin.site.register(Rubric)
