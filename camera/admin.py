from django.contrib import admin
from .models import *

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0  # Removes extra empty forms

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    inlines = [AnswerInline]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')

# Register your models here
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)