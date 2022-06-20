from django.shortcuts import render
from Volunteers.forms import VolunteerRegistrationForm


def index(request):
    return render(request, 'index.html', {})


def logout(request):
    return render(request, 'index.html', {})


def VolunteerLogin(request):
    return render(request, 'VolunteerLogin.html', {})


def AdminLogin(request):
    return render(request, 'AdminLogin.html', {})


def VolunteerRegister(request):
    form = VolunteerRegistrationForm()
    return render(request, 'VolunteerRegister.html', {'form': form})
