from django.contrib import admin
from .models import *

# Defines admin interface for the Question model
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 0  

# Defines admin interface for the Answer model
class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0

# Custom admin interface for the Quiz model
class QuizAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [QuestionInline]

# Custom admin interface for the Question model
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz')
    inlines = [AnswerInline]

# Custom admin interface for the Answer model
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)