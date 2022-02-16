from re import search
from django.contrib import admin
from .models import Motabari3

# Register your models here.
class Motabari3Admin(admin.ModelAdmin):
    list_display=['name','age','wilaya','commun']
    list_filter=['age','wilaya','commun']
    search_fields=['name','wilaya']
admin.site.register(Motabari3,Motabari3Admin)