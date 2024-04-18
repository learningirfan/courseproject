from django.contrib import admin
from expenses.models import Exps

# Register your models here.
class ExpsAdmin(admin.ModelAdmin):
    """ Admin Interface for Exps """

admin.site.register(Exps)