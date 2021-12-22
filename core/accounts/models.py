from django.db import models
from django.contrib.auth.models import AbstractUser
from questions.models import SubjectModel, QuestionsModel


class AdvUser(AbstractUser):
    current_subject = models.ForeignKey(SubjectModel,
                                        on_delete=models.SET_NULL,
                                        verbose_name='Текущий предмет',
                                        related_name='current_subject',
                                        null=True,
                                        blank=True)
    all_questions = models.ManyToManyField(QuestionsModel,
                                           related_name='all_questions',
                                           )
    current_questions = models.ForeignKey(QuestionsModel,
                                          on_delete=models.SET_NULL,
                                          verbose_name='Текущий вопрос',
                                          null=True,
                                          blank=True)

    email = models.EmailField('Почта', unique=True)

    def __str__(self):
        return self.email