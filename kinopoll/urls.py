from django.urls import include, path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'polls', views.PollViewSet)
router.register(r'questions', views.QuestionViewSet, 'question')
router.register(r'options', views.OptionViewSet, 'option')

urlpatterns = [
    path('', include(router.urls)),
]