from django.db import models
#　変更したら
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class location(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=5)
    
class weather(models.Model):
    location = models.CharField(max_length = 5)
    windspeed = models.CharField(max_length = 2)

class currentConditions(models.Model):
    zipcode = models.CharField(max_length = 5)
    temperature = models.CharField(max_length = 3)
    windspeed = models.CharField(max_length = 2)





#class currentWeather():
#    conditions = ["Sunny","No Wind","Warm","75F"]
#    info = {"temp":"75", "humid":"50%","wind":"0mph"}
#    multiWeather = [{"local":"Belleville","temp":"75", "humid":"50%","wind":"0mph"},{"local":"Russellville","temp":"75", "humid":"50%","wind":"0mph"}]