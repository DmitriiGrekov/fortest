from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from questions.models import SubjectModel
from .forms import LoginForm, UserRegisterForm

import random


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,
                                username=username,
                                password=password)
            if user is None:
                messages.error(request,
                               'Вы ввели не правильный логин или пароль')
                return render(request, 'includes/modal_auth.html')
            else:
                login(request, user)
                messages.success(request, 'Вы успешно авторизованы')
                return JsonResponse({'status': 302})

            print('good')


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Вы успешно вышли из аккаунта')
        return redirect('index')


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Вы успешно зарегестрированны, можете авторизоваться')
            return JsonResponse({'status': 201})
        else:
            return JsonResponse({'errors': form.errors})


def current_subject_user(request):
    if request.method == 'POST':
        if 'subject_pk' in request.POST:
            subject_pk = int(request.POST.get('subject_pk'))
        current_subject = SubjectModel.objects.get(pk=subject_pk)
        request.user.current_subject = current_subject
        # subject_questions = current_subject.questions.all()
        # user_questions = request.user.all_questions.all()
        # flag = True

        # while flag:
        #     random_question = random.choice(subject_questions)
        #     if random_question not in user_questions:
        #         request.user.all_questions.add(random_question)
        #         flag = False
        request.user.all_questions.clear()
        if len(current_subject.questions.all()) == 0:
            request.user.current_questions = None
            request.user.all_questions.clear()
            request.user.save()
            return JsonResponse({'status': 500, 'message': 'Вы не добавили ни одного вопроса'})
        current_question = random.choice(current_subject.questions.all())
        request.user.current_questions = current_question
        request.user.all_questions.add(current_question)
        request.user.save()
        return JsonResponse({'status': 201})


def next_random_question(request, subject_pk):
    if request.user.is_authenticated:
        current_subject = SubjectModel.objects.get(pk=subject_pk)
        user_questions = request.user.all_questions.all()
        flag = True
        if len(user_questions) == len(current_subject.questions.all()):
            print('очищаем все вопросы')
            request.user.all_questions.clear()
            return next_random_question(request, subject_pk)

        while flag:
            random_question = random.choice(current_subject.questions.all())
            print(random_question not in user_questions)
            if random_question not in user_questions:
                print('добавляем новый вопрос')
                request.user.all_questions.add(random_question)
                request.user.current_questions = random_question
                request.user.save()
                flag = False
            if len(user_questions) == len(current_subject.questions.all()):
                flag = False
        return redirect('index')
