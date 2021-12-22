from django.db import models
from django.conf import settings


class SubjectModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE,
                               verbose_name='Автор')
    description = models.TextField(verbose_name='Описание предмета',
                                   blank=True,
                                   null=True)
    create_date = models.DateTimeField(verbose_name='Дата создания',
                                       auto_now_add=True)
    
    def __str__(self):
        return f'Предмет "{self.title}" автора -> {self.author.username}'
    
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы' 


class QuestionsModel(models.Model):
    subject = models.ForeignKey(SubjectModel,
                                on_delete=models.CASCADE,
                                verbose_name='Предмет',
                                related_name='questions')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    question = models.TextField(blank=True, null=False)

    def __str__(self):
        return f'Вопрос по предмету {self.subject} -> {self.question}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class AnswerModel(models.Model):
    subject = models.ForeignKey(SubjectModel,
                                on_delete=models.CASCADE,
                                related_name='answers'
                                )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    question = models.ForeignKey(QuestionsModel,
                                 on_delete=models.CASCADE,
                                 related_name='answer_question')
    answer = models.TextField(blank=True, null=False)

    def __str__(self):
        return f'Ответ на вопрос {self.question}'
    
    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
