from django.urls import path
from .views import WordsListView


urlpatterns = [
    path("start/", WordsListView.as_view(), name="index"),
]