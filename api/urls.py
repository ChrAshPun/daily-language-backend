from django.urls import path
from .views import SpanishWordList, ITArticleList

urlpatterns = [
    path('spanishdict/', SpanishWordList.as_view()),
    path('itarticles/', ITArticleList.as_view()),
]