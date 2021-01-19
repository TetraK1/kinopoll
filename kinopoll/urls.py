from django.urls import include, path

from rest_framework import routers

from . import views

#router = routers.DefaultRouter()
#router.register(r'polls', views.PollViewSet)
#router.register(r'polls/<int:pk>/questions', views.TextQuestionViewSet)
#router.register(r'responses', views.ResponseViewSet)

#urlpatterns = [
#    path('', include(router.urls)),
#]

urlpatterns = [
    path('polls/', views.PollViewSet.as_view({'get': 'list'})),
    path('polls/<int:pk>/', views.PollViewSet.as_view({'get': 'retrieve'})),

    path('polls/<int:poll_id>/questions/', views.QuestionViewSet.as_view({'get': 'list'})),
    path('polls/<int:poll_id>/questions/<int:pk>/', views.QuestionViewSet.as_view({'get': 'retrieve'}), name='question-detail'),

    path('polls/<int:poll_id>/responses/', views.ResponseViewSet.as_view({'get': 'list'})),
    path('polls/<int:poll_id>/responses/<int:pk>/', views.ResponseViewSet.as_view({'get': 'retrieve'})),
]

