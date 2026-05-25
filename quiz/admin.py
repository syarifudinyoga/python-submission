from django.contrib import admin
from .models import (
    Question,
    Choice,
    Submission,
    Lesson,
    Category,
    Student,
    Teacher
)


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text')
    search_fields = ('question_text',)
    inlines = [ChoiceInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    inlines = [QuestionInline]


admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Category)
admin.site.register(Student)
admin.site.register(Teacher)