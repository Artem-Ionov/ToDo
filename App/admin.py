from django.contrib import admin
from .models import Task, Question, Question_block

admin.site.register(Task)
admin.site.register(Question)
#admin.site.register(Question_block)

class QuestionInline(admin.TabularInline):
    model=Question
    extra=0

class Question_blockAdmin(admin.ModelAdmin):
    inlines=[QuestionInline]

admin.site.register(Question_block, Question_blockAdmin)
