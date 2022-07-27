from django import forms 
from .models import Question, Answer

class questionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question']
        

class answerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer']
        
