from django.db import models
from django.template import loader

from polymorphic.models import PolymorphicModel

from model_utils.managers import InheritanceManager

# Base classes
class Poll(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #creation date
    #owner
    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.title}'

class Response(models.Model):
    #date
    #user
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='responses')

class Question(PolymorphicModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

class Answer(PolymorphicModel):
    response = models.ForeignKey(Response, models.CASCADE)
    question = models.ForeignKey(Question, models.CASCADE)

# Text Question
class TextQuestion(Question):
    pass

class TextAnswer(Answer):
    answer_text = models.CharField(max_length=200)

# Multiple Choice Question
class MultipleChoiceQuestion(Question):
    pass

class MultipleChoiceOption(models.Model):
    text = models.CharField(max_length=200)

class MultipleChoiceAnswer(Answer):
    choice = models.ForeignKey(MultipleChoiceOption, models.CASCADE)

# Ranking Question
class RankedQuestion(Question):
    pass

class RankedOption(models.Model):
    question = models.ForeignKey(RankedQuestion, models.CASCADE)
    text = models.CharField(max_length=200)

class RankedAnswer(Answer):
    option = models.ForeignKey(RankedOption, models.CASCADE)
    ranking = models.IntegerField()