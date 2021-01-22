from django.contrib.auth.models import User, Group
from rest_framework import serializers

from kinopoll import models

class OptionSerializer(serializers.ModelSerializer):
    question = serializers.HyperlinkedRelatedField(view_name='question-detail', read_only=True)
    class Meta:
        model = models.Option
        fields = ['id', 'question', 'position', 'text']

class QuestionSerializer(serializers.ModelSerializer):
    poll = serializers.HyperlinkedRelatedField(view_name='poll-detail', read_only=True)
    option_set = serializers.HyperlinkedRelatedField(many=True, view_name='option-detail', read_only=True)
    class Meta:
        model = models.Question
        fields = ['id', 'poll', 'question_type', 'title', 'description', 'option_set']

class PollSerializer(serializers.ModelSerializer):
    question_set = serializers.HyperlinkedRelatedField(many=True, view_name='question-detail', read_only=True)
    class Meta:
        model = models.Poll
        fields = ['id', 'title', 'description', 'question_set']