from django.db import models
from django.template import loader

class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

class Question(models.Model):
    class QuestionTypes(models.TextChoices):
        TEXT = 'TEXT'
        RANKED = 'RANKED'
        MULTIPLE_CHOICE = 'MULTIPLE_CHOICE'

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='questions')
    question_type = models.CharField(max_length=50, choices=QuestionTypes.choices, default=QuestionTypes.TEXT)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

class Option(models.Model):
    #extra data needed by any questions, e.g. options for multiple choice questions
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    position = models.IntegerField(blank=True)
    text = models.TextField(blank=True)
    #data can be switched on later when moving to postgres
    #data = models.JSONField()

    def __str__(self):
        return f'{self.question.title} - {self.text[:50]}'
