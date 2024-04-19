from .views import MainView, AddNew, ExpEdit
from django.urls import path
from . import views


urlpatterns = [
    path("", MainView.as_view(), name="Main"),
    path("create/", AddNew.as_view(), name="create"),
    path("<pk>/edit", ExpEdit.as_view(), name="edit"),

]