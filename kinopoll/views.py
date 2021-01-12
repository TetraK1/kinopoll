from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from . import models

# Create your views here.
def index(request):
    polls = models.Poll.objects.all()
    return render(request, 'kinopoll/index.html', {'polls': polls})

def vote(request, poll_id):
    poll = get_object_or_404(models.Poll, pk=poll_id)
    questions = poll.question_set
    return render(request, 'kinopoll/vote/vote.html', {'poll': poll})