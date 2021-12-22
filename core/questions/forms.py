from ckeditor import fields
from django import forms
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from .models import SubjectModel, QuestionsModel, AnswerModel
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class AddSubjectForm(forms.ModelForm):

    class Meta:
        model = SubjectModel
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Название предмета'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
                                                 'placeholder': 'Описание'})
        }


class QuestionForm(forms.Form):
    question = forms.CharField(widget=CKEditorUploadingWidget, label='Вопрос')
    answer = forms.CharField(widget=CKEditorUploadingWidget, label='Ответ')


QuestionFormSet = formset_factory(QuestionForm)