from django.contrib import admin
from .models import SpanishWord

class SpanishWordAdmin(admin.ModelAdmin):
    list_display = ['spa', 'pronunciation', 'eng', 'created_on', 'updated_on']
    readonly_fields = ('created_on', 'updated_on')

admin.site.register(SpanishWord, SpanishWordAdmin) # add to admin panel
