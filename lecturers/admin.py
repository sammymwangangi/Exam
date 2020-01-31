from django.contrib import admin
from .models import Lecturer

class LecturerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('name', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['name']

admin.site.register(Lecturer, LecturerAdmin)