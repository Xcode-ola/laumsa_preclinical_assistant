from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Courses)
admin.site.register(Quiz)
admin.site.register(PracticeQuestions)
admin.site.register(Chapters)
admin.site.register(Summary)

class StemInLineTable(admin.TabularInline):
    model = QuestionStem
    fields = [
        'body',
        'ans',
    ]

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'quiz',
        'question',
    ]
    list_display = [
        'quiz',
        'question',
    ]
    inlines = [
        StemInLineTable,
    ]

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'body',
        'ans'
    ]

admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionStem, AnswerAdmin)