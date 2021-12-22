from django.contrib import admin
from .models import SubjectModel, QuestionsModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget 
from django import forms
from .models import QuestionsModel, AnswerModel


class QuestionAdminForm(forms.ModelForm):
    question = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = QuestionsModel
        fields = '__all__'


class AnswerAdminForm(forms.ModelForm):
    answer = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = AnswerModel 
        fields = '__all__'


@admin.register(SubjectModel)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'author',
                    'description',
                    'create_date')
    form = QuestionAdminForm


@admin.register(QuestionsModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'question')


@admin.register(AnswerModel)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('subject', 'user', 'question', 'answer')
    form = AnswerAdminForm