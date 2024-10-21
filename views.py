from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import weather
from .models import location
from .models import currentConditions

from django.http import HttpResponseRedirect
from .forms import LocationForm, ConditionsForm

# Create your views here.
def index(request):
    #weatherObject = weather.objects.all().values()

    locationObject = location.objects.all().values()
    if request.method=="POST":
        form = LocationForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            zip = form.cleaned_data['zip']
            l = location(city=city, state=state, zip=zip)
            l.save()

            context = {
                'local':locationObject,
                #'formData':form
            }
            template = loader.get_template('submitted.html');
            return HttpResponse(template.render(context, request))
    else:
        form = LocationForm()

        form2 = ConditionsForm()

    context = {
        'form':form,
        'form2':form2
    }

    template = loader.get_template('index.html');
    return HttpResponse(template.render(context, request))
