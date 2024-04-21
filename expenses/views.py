from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Exps
from .forms import ExpsForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.

#Here is the main view where data gets displayed
class MainView(ListView):
    template_name = "main.html"
    context_object_name = "exp_list"

    def get_queryset(self):
        return Exps.objects.all()
    
#This view class is for adding new data row into expenses
class AddNew(CreateView):
    model = Exps
    form_class = ExpsForm
    template_name = "create.html"
    success_url = reverse_lazy("Main")

#This view class is for editing an existing data row
class ExpEdit(UpdateView):
    model = Exps
    form_class = ExpsForm
    template_name = "edit.html"
    success_url = reverse_lazy("Main")
        
#This view class is for deleting an existing data row
class ExpDelete(DeleteView):
    model = Exps
    template_name = "delete.html"
    success_url = reverse_lazy("Main")