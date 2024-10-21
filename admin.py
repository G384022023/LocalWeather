from django.contrib import admin
from .models import weather, location

#Register your models here.
#class LocationFormadmin (admin.FormAdmin):
#    list_display = ("zip", "state" ,)

class weatheradmin (admin.ModelAdmin):
    list_display = ("location", "windspeed",)

class locationadmin (admin.ModelAdmin):
    list_display = ("city", "state", "zip")

#class currentConditionsadmin (admin.ModelAdmin):
#    list_display = ("zipcode", "temperature" , "windspeed")

#admin.site.register(LocationForm, LocationFormadmin)
admin.site.register(weather, weatheradmin)
admin.site.register(location, locationadmin)
#admin.site.register(currentConditions, currentConditionsadmin)

