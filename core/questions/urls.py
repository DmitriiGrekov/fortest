from django.urls import path
from .views import (add_subject_view,
                    subject_list,
                    delete_subject_view,
                    add_question_view,
                    show_all_questions,
                    delete_questions)


app_name = 'questions'
urlpatterns = [
    path('add/', add_subject_view, name='add'),
    path('subject/list/', subject_list, name='list'),
    path('subject/delete/<int:pk>/',
         delete_subject_view,
         name='delete'),
    path('question/add/<int:subject_pk>/',
         add_question_view,
         name='add_question'),
    path('questions/all/<int:subject_pk>/',
         show_all_questions,
         name='all_questions'),
    path('questions/delete_questions/<int:question_pk>/',
         delete_questions,
         name='delete_questions')
]
