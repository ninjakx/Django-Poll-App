from django.contrib import admin

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['polls_heading']}),
        
    ]
    inlines = [ChoiceInline]
    list_display = ('polls_heading', 'created_at', 'updated_at')
    
    list_filter = ['polls_heading']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
