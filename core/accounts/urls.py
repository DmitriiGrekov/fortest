from django.urls import path
from .views import (user_login,
                    user_logout,
                    user_register,
                    current_subject_user,
                    next_random_question)


app_name = 'accounts'
urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('add/current_subject/',
         current_subject_user,
         name='add_current_subject'),
    path('get/random/question/<int:subject_pk>/',
         next_random_question,
         name='random_question')
]
