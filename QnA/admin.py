from django.contrib import admin

# Register your models here.
from .models import Question, Answer
class QuestionAdmin(admin.ModelAdmin):
    list_display=['id', 'photo', 'question']
    raw_id_fields = ['photo']
    list_filter = ['photo'] 


class AnswerAdmin(admin.ModelAdmin):
    list_display=['id', 'question', 'answer']
    raw_id_fields = ['question']
    list_filter = ['question'] 


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)