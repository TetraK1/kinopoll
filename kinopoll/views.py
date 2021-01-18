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

#class QuestionViewSet(viewsets.ModelViewSet):
#    queryset = models.Question.objects.all()
#    serializer_class = serializers.QuestionSerializer

class ResponseViewSet(viewsets.ModelViewSet):
    queryset = models.Response.objects.all()
    serializer_class = serializers.ResponseSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'polls': reverse('poll-list', request=request, format=format),
    })