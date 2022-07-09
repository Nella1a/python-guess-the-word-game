from django.shortcuts import render
from .models import SecretWords
from django.views.generic.list import ListView
# Create your views here.
#from django.http import HttpResponse



class WordsListView(ListView):
    model = SecretWords
    template_name = "guess_app/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context