from django.test import TestCase
from rest_framework.test import APIRequestFactory
from kinopoll.views import PollViewSet

# Create your tests here.
class PostTest(TestCase):
    def test_poll_post(self):
        factory = APIRequestFactory()
        request = factory.post('/polls/', {
            "title": "post test 2",
            "description": "tink",
            "question_set": [
                {
                    "question_type": "TEXT",
                    "title": "TQ TITLE",
                    "description": "TQ DESC",
                    "option_set": []
                }
            ]
        })

        from kinopoll.models import Poll
        view = PollViewSet.as_view({'post': 'create'})
        response = view(request)
        print(response.data)
        print(Poll.objects.all())