from django.views import View
from django.shortcuts import render, redirect

from myapp1.forms import AddVehicleForm

class Vehicle(View):

    def get(self, request):#read
        form = AddVehicleForm()
        return render(request, 'addVehicle.html', {'form': form})

    def post(self, request):#create
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



