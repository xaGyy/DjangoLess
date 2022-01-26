from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from myapp1.models import Brand, Vehicle
import json
from myapp1.forms import AddVehicleForm

menu_list = ["header", "menu", "first page", "about", "footer"]


def sayHello(request):
    return render(request, 'hello.html', {"title": "Главная страница",
                                          "page": "Страница для сайта",
                                          "menu_list": menu_list}
                  )


def sayH1(request):
    return render(request, 'helloh1.html', {"title": "Вторая страница",
                                            "page": "Страница для сайта2",
                                            "menu_list": menu_list
                                            }
                  )


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {
        "title": "Список автомобилей",
        "cars": cars
    })


def get_brands(request):
    brands = Brand.objects.all()
    return render(request, 'brand_list.html', {
        "title": "Вторая страница",
        "brands": brands
    })

def get_brands_by_country(request):
    brands = Brand.objects.filter(country="Germany")
    return render(request, 'brand_list.html', {
        "title": "Вторая страница",
        "brands": brands
    })

def get_vehicle_by_brand(request):
    brand = Brand.objects.get(name="Mercedes")
    cars = brand.get_vehicles.all()
    # cars = brand.vehicle_set
    return render(request, 'car_list.html', {
        "title": "Вторая страница",
        "cars": cars
    })

def get_vehicle_by_brands(request):
    cars = []
    brands = Brand.objects.filter(name__in=['Audi', 'Mercedes', 'BMW'])
    for brand in brands:
        for car in brand.get_vehicles.all():
            cars.append(car)
    print(cars)
    return render(request, 'car_list.html', {
            "title": "Вторая страница",
            "cars": cars
        })

def addVehicle(request):
    if request.method == 'POST':
        form = AddVehicleForm(request.POST)
        print(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                #Vehicle.objects.create(**form.cleaned_data)
                form.save()
                return redirect('add_page')
            except:
                form.add_error(None, "Ошибка добавления")
    else:
        form = AddVehicleForm()
    return render(request, 'addVehicle.html', {'form': form})


def deleteVehicle(request, pk):
    try:
        vehicle = Vehicle.objects.get(id = pk)
        print(vehicle)
        vehicle.delete()
    except:
        print("Error")

def getVehicleById(request, pk):
    form = None
    try:
        vehicle = Vehicle.objects.get(id=pk)
        form = AddVehicleForm(initial=model_to_dict(vehicle))
        return render(request, 'addVehicle.html', {'form': form})
        print(vehicle)

    except:
        print("Error")

#не работает
def updateVehicle(request, pk):
    if request.method == "GET":
        vehicle = Vehicle.objects.get(id=pk)
        form = AddVehicleForm(initial=model_to_dict(vehicle))
        return render(request, 'updateVehicle.html', {'form': form, 'pk': pk})
    elif request.method == "POST":
        vehicle = Vehicle.objects.get(id=pk)
        form = AddVehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
        return redirect('update_page')