from django.contrib.auth.models import User, Group
from rest_framework import serializers
from kinopoll.models import *

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'poll']

class MultipleChoiceOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceOption
        fields = ['text']

class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    options = MultipleChoiceOptionSerializer(many=True)
    class Meta:
        model = MultipleChoiceQuestion
        fields = QuestionSerializer.Meta.fields + ['options']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question', 'response']

class ResponseSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Response
        fields = ['poll', 'answers']

class PollSerializer(serializers.ModelSerializer):
    #questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Question.objects.all())
    questions = QuestionSerializer(many=True)
    #responses = serializers.PrimaryKeyRelatedField(many=True, queryset=Response.objects.all())
    #responses = ResponseSerializer(many=True)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'questions']