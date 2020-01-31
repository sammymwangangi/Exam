from django.contrib import admin
from .models import Exam

class ExamAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['exam_text', 'answer', ]}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('exam_text', 'answer', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['exam_text']

admin.site.register(Exam, ExamAdmin)