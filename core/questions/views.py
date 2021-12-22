from django.contrib.messages.api import success
from django.forms.models import inlineformset_factory
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.forms import inlineformset_factory
from .forms import AddSubjectForm, QuestionFormSet
from .models import AnswerModel, QuestionsModel, SubjectModel
import json


def subject_list(request):
    if request.user.is_authenticated:
        user = request.user
        subjects = SubjectModel.objects.filter(author=user).order_by('-create_date')
        return render(request,
                      'questions/subject_list.html',
                      {'subjects': subjects})



def add_subject_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddSubjectForm(request.POST)
            if form.is_valid():
                subject = form.save(commit=False)
                subject.author = request.user
                subject.save()
                messages.success(request, f'Предмет {subject.title} добавлен')
                return redirect('questions:list')
    else:
        messages.error(request, 'Чтобы добавить предмет, необходима авторизация')
        return redirect('/')


def delete_subject_view(request, pk):
    if request.user.is_authenticated:
        subject = SubjectModel.objects.get(pk=pk)
        if subject.author == request.user:
            subject.delete()
            messages.success(request, f'Предмет {subject.title} удален')
            return redirect('questions:list')


def add_question_view(request, subject_pk):
    if request.user.is_authenticated:
        subject = SubjectModel.objects.get(pk=subject_pk)
        if request.method == 'POST':
            data = request.POST
            data = dict(data)
            print(len(data))
            for key in data:
                print(key)
                if key == 'csrfmiddlewaretoken':
                    continue
                question = QuestionsModel.objects.create(subject=subject,
                                                         user=request.user,
                                                         question=data[key][0])
                question.save()

                answer = AnswerModel.objects.create(subject=subject,
                                                    user=request.user,
                                                    question=question,
                                                    answer=data[key][1])
                answer.save()
                print(answer)
            messages.success(request, f'Вопросы по предмету {subject.title} успешно добавлены')
            return JsonResponse({'status': 201})
        else:
            return render(request,
                      'questions/add_question_and_subject.html',
                      {'subject_pk': subject_pk,
                       'subject': subject})


def show_all_questions(request, subject_pk):
    subject = SubjectModel.objects.get(pk=subject_pk)
    return render(request,
                  'questions/questions_list.html',
                  {'subject': subject})


def delete_questions(request, question_pk):
    question = get_object_or_404(QuestionsModel, pk=question_pk)
    question.delete()
    messages.success(request, f'Вопрос успешно удален')
    return redirect(request.META.get('HTTP_REFERER'))
