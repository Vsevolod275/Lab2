from django.shortcuts import render

def home(request):
    return render(request, 'rental/home.html')

def cars(request):
    return render(request, 'rental/cars.html')

def car_detail(request, car_id):
    return render(request, 'rental/car_detail.html', {'car_id': car_id})

def about(request):
    return render(request, 'rental/about.html')

def contact(request):
    return render(request, 'rental/contact.html')
