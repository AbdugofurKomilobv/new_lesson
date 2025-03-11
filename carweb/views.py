from django.shortcuts import render

from .models import Cars

def car_pages(request):
    car = Cars.objects.all()
    context = {
        'car': car,
        'title': 'Car pages'
    }
    return render(request=request,template_name='car.html',context=context)
