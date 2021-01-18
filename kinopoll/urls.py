from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'polls', views.PollViewSet)
#router.register(r'questions', views.QuestionViewSet)
router.register(r'responses', views.ResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]