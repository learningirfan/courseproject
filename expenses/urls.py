from .views import MainView, AddNew, ExpEdit, ExpDelete
from django.urls import path
from . import views


urlpatterns = [
    path("", MainView.as_view(), name="Main"),
    path("create/", AddNew.as_view(), name="create"),
    path("edit/<int:pk>/", ExpEdit.as_view(), name="edit"),
    path("delete/<int:pk>/", ExpDelete.as_view(), name="delete")

]