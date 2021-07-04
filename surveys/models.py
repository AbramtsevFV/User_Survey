from django.db import models
from django.db.models import CharField, TextField, DateTimeField, ForeignKey, IntegerField




class Survey(models.Model):
    name = CharField(max_length=150, verbose_name='Название опроса')
    start_date = DateTimeField(verbose_name="Дата старта опроса")
    end_date = DateTimeField(verbose_name="Дата окончания опроса")
    survey_description = TextField(verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name
    

class Question(models.Model):
    class Type:
        TEXT = 'TEXT'
        CHOICE = 'CHOICE'
        MULTICHOICE = 'MULTICHOICE'

        choices = (
            (TEXT, 'TEXT'),
            (CHOICE, 'CHOICE'),
            (MULTICHOICE, 'MULTICHOICE'),
        )
    survey = ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    question = CharField(max_length=150, verbose_name='Вопрос')
    question_type = CharField(max_length=50, choices=Type.choices, default=Type.TEXT,  verbose_name='Тип вопроса')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return str(self.question)

class Variants(models.Model):
    question = ForeignKey(Question, related_name='variants', on_delete=models.CASCADE)
    answer_option = CharField(max_length=200, verbose_name='Вариант ответа')

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return str(self.question)

class Answer(models.Model):
    user_id = IntegerField(verbose_name='id Пользователя')
    survey = ForeignKey(Survey, related_name='survey', on_delete=models.CASCADE)
    quest = ForeignKey(Question, related_name='quest', on_delete=models.CASCADE)
    variant = ForeignKey(Variants, related_name='variant', on_delete=models.CASCADE,
                         blank=True, null=True)
    variant_text = CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.user_id)
