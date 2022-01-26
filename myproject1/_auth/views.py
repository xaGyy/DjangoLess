from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import createUserForm

def registration(request):
    if request.method == "POST":
        form = createUserForm(request.POST)
        if form.is_valid():
            try:
                print(form.cleaned_data)
                user = User.objects.create_user(**form.cleaned_data)
                user.save()
                return redirect('add_user')
            except:
                form.add_error(None, "Ошибка добавления")
    else:
        form = createUserForm()

    return render(request, 'signup.html', {'form': form})


# Create your views here.