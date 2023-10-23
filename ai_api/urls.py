from django.urls import path
from .views.ask_question import AskQuestion
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', AskQuestion.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)