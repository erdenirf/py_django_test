from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Car
from .forms import ManufacturersForm

def index(request):

    if request.method == 'POST':

        form = ManufacturersForm(request.POST)
        if form.is_valid():
            
            car_model = form.cleaned_data['car_model']
            if car_model != '0':
                
                cars_all = Car.objects.filter(manufacturer=car_model)
            else:
                cars_all = Car.objects.all()

    # if a GET
    else:
        form = ManufacturersForm()
        cars_all = Car.objects.all()

    template = loader.get_template('polls/index.html')
    context = {
        'cars_all': cars_all,
        'form': form,
    }
    return HttpResponse(template.render(context, request))

