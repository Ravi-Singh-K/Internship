from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Question)
class QuestionsAdminDisplay(admin.ModelAdmin):
    model = Question
    list_display = ('question_text', 'pub_date__year', 'pub_date__time')



admin.site.register(Question, QuestionsAdminDisplay)