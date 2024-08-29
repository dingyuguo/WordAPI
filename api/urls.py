from django.urls import path
from .views import get_word

urlpatterns = [
    path('get_word/', get_word),
]
