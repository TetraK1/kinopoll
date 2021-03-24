from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import response, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from . import models, serializers

class PollViewSet(viewsets.ModelViewSet):
    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        queryset = models.Question.objects.all()
        poll_id = self.request.query_params.get('poll', None)
        if poll_id is not None: queryset = queryset.filter(poll__id=poll_id)
        return queryset

class OptionViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OptionSerializer

    def get_queryset(self):
        queryset = models.Option.objects.all()
        question_id = self.request.query_params.get('question', None)
        if question_id is not None: queryset = queryset.filter(question__id=question_id)
        return queryset

#@api_view(['GET'])
#def api_root(request, format=None):
#    return Response({
#        'polls': reverse('poll-list', request=request),
#        'questions': {
#            reverse('text-questions-list', request=request),
#        },
#    })