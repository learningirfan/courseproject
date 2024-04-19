from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Exps
from .forms import ExpsForm
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.
class MainView(ListView):
    template_name = "main.html"
    context_object_name = "exp_list"

    def get_queryset(self):
        return Exps.objects.all()
    

class AddNew(CreateView):
    model = Exps
    form_class = ExpsForm
    template_name = "create.html"
    success_url = reverse_lazy("Main")

class ExpEdit(UpdateView):
    model = Exps
    fields =["date", "amt", "cat", "ven", "cap", "pmeth"]
    success_url = reverse_lazy("Main")
    

