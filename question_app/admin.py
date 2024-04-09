from django.contrib import admin
from .models import User,Department,Course,Topic,Answer,Question

# Register your models here.
admin.site.register(User)
admin.site.register(Department)

class TopicInline(admin.TabularInline):
    model = Topic

class CourseAdmin(admin.ModelAdmin):
    inlines = [TopicInline]


admin.site.register(Course, CourseAdmin)
admin.site.register(Topic)

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
     inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin )
admin.site.register(Answer)
