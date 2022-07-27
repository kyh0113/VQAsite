from django.db.models import fields
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Question, Answer, Photo
from django.contrib.auth.decorators import login_required
from django import forms
from . import models
from .forms import questionForm, answerForm

# from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required

# 사진 번호에 맞게 질문이 저장되어야 함

@login_required
def question_view(request, photo_pk):
    photo = get_object_or_404(Photo, pk=photo_pk)
    if request.method=='POST':
        form = questionForm(request.POST, request.FILES)
        if form.is_valid():
            qst = form.save(commit=False)
            qst.photo = photo
            qst.author = request.user
            qst.save()
            return redirect('QnA:answer_view', qst.pk)
    else:
        form = questionForm()
    return render(request, "QnA/question.html", {'form':form})


@login_required
def answer_view(request, question_pk):
    question= get_object_or_404(Question, pk=question_pk)
    if request.method=="POST":
        form = answerForm(request.POST, request.FILES)
        if form.is_valid():
            ans = form.save(commit=False)
            ans.question=question
            ans.author = request.user
            ans.save()
            return redirect('photo:photo_view')
    else:
        form = answerForm()
    return render(request, "QnA/answer.html", {'form':form})