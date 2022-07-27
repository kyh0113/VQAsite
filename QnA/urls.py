from django.urls import path
from . import views
# from .views import *

app_name="QnA"

urlpatterns = [
    path("QnA/<int:photo_pk>/question/", views.question_view, name='question_view'),
    path('QnA/<int:question_pk>/answer/', views.answer_view, name="answer_view"),
]
