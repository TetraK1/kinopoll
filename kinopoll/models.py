from django.db import models
from django.template import loader

from model_utils.managers import InheritanceManager

# Base classes
class Poll(models.Model):
    title = models.CharField(max_length=200)

    def render_vote(self):
        template = loader.get_template('kinopoll/vote/poll.html')
        questions = self.question_set.all().select_subclasses()
        return template.render({'poll': self, 'questions': questions})

class Response(models.Model):
    pass

class Question(models.Model):
    text = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    # adds select_subclasses() as a method on querysets that turns all
    # instances in the set into their actual subclass
    objects = InheritanceManager()
    
    def render_vote(self):
        template = loader.get_template('kinopoll/vote/question.html')
        return template.render({'question': self})

class Answer(models.Model):
    response = models.ForeignKey(Response, models.CASCADE)
    question = models.ForeignKey(Question, models.CASCADE)

# Text Question
class TextQuestion(Question):
    def render_vote(self):
        template = loader.get_template('kinopoll/vote/textquestion.html')
        return template.render({'question': self})

class TextAnswer(Answer):
    answer_text = models.CharField(max_length=200)

# Multiple Choice Question
class MultipleChoiceQuestion(Question):
    def render_vote(self):
        template = loader.get_template('kinopoll/vote/multiplechoicequestion.html')
        return template.render({'question': self, 'options': self.multiplechoiceoption_set.all()})

class MultipleChoiceOption(models.Model):
    question = models.ForeignKey(MultipleChoiceQuestion, models.CASCADE)
    text = models.CharField(max_length=200)

class MultipleChoiceAnswer(Answer):
    choice = models.ForeignKey(MultipleChoiceOption, models.CASCADE)

# Ranking Question
class RankedQuestion(Question):
    def render_vote(self):
        template = loader.get_template('kinopoll/vote/rankedquestion.html')
        return template.render({'question': self, 'options': self.rankedoption_set.all()})

class RankedOption(models.Model):
    question = models.ForeignKey(RankedQuestion, models.CASCADE)
    text = models.CharField(max_length=200)

class RankedAnswer(Answer):
    option = models.ForeignKey(RankedOption, models.CASCADE)
    ranking = models.IntegerField()