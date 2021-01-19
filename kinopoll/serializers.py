from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from kinopoll.models import *

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'poll']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'title', 'description']

class TextQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'title', 'description']

class RankedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'title', 'description']

class MultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'poll', 'title', 'description']

class QuestionPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        Question: QuestionSerializer,
        TextQuestion: TextQuestionSerializer,
        MultipleChoiceQuestion: MultipleChoiceQuestionSerializer,
        RankedQuestion: RankedQuestionSerializer,
    }

class PollSerializer(serializers.ModelSerializer):
    questions = QuestionPolymorphicSerializer(source='question_set', many=True)
    class Meta:
        model = Poll
        fields = ['id', 'title', 'description', 'questions']