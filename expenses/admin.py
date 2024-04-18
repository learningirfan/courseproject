from django.contrib import admin
from expenses.models import Exps

# Register your models here.
class ExpsAdmin(admin.ModelAdmin):
    """ Admin Interface for Exps """
    list_display = ["date", "amt", "cat", "ven", "cap", "pmeth"]

admin.site.register(Exps, ExpsAdmin)
