from django import template
from django.shortcuts import render
from django.views.generic.base import TemplateView
from accounts.forms import LoginForm, UserRegisterForm
from questions.forms import AddSubjectForm


class IndexView(TemplateView):
    template_name = 'main/index.html'

    

