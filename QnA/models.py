from django.db import models
# from django.core.validators import MinLengthValidator

from photo.models import Photo

# Create your models here.


class Question(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE, related_name='photo_questions') # 1:n (사진 1개 : 여러개 질문 n) 사진이 삭제되면 질문을 전부 지우겠음 CASCADE
    question = models.CharField(max_length=500)
   

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE) # 1:1 (질문 1개 : 답변 1개)    질문이 삭제되면 답변을 전부 지우겠음 
    answer = models.CharField(max_length=500)
    
    
    
    