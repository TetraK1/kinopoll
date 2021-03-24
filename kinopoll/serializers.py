from django.contrib.auth.models import User, Group
from rest_framework import serializers

from kinopoll import models

class OptionSerializer(serializers.ModelSerializer):
    question = serializers.HyperlinkedRelatedField(view_name='question-detail', read_only=True)
    class Meta:
        model = models.Option
        fields = ['id', 'question', 'position', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.HyperlinkedRelatedField(view_name='option-detail', many=True, read_only=True)
    poll = serializers.HyperlinkedRelatedField(view_name='poll-detail', read_only=True)
    class Meta:
        model = models.Question
        fields = ['id', 'poll', 'question_type', 'title', 'description', 'options']

class PollSerializer(serializers.ModelSerializer):
    questions = serializers.HyperlinkedRelatedField(view_name='question-detail', many=True, read_only=True)
    class Meta:
        model = models.Poll
        fields = ['id', 'title', 'description', 'questions']