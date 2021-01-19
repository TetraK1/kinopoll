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
    serializer_class = serializers.QuestionPolymorphicSerializer

    def get_queryset(self):
        poll = self.kwargs['poll_id']
        return models.Question.objects.filter(poll__id=poll)

class ResponseViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ResponseSerializer

    def get_queryset(self):
        poll = self.kwargs['poll_id']
        return models.Question.objects.filter(poll__id=poll)
    


#@api_view(['GET'])
#def api_root(request, format=None):
#    return Response({
#        'polls': reverse('poll-list', request=request),
#        'questions': {
#            reverse('text-questions-list', request=request),
#        },
#    })