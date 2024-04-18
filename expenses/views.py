from django.shortcuts import render
from .models import Exps
from .forms import ExpsForm
from django.views.generic import ListView

# Create your views here.
class MainView(ListView):
    template_name = "main.html"
    context_object_name = "exp_list"

    def get_queryset(self):
        return Exps.objects.all()