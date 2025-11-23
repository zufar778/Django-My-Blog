from django.shortcuts import render, redirect
from .models import Person


# Create your views here.

def Index_views(request):
    persons = Person.objects.all()
    return render(request, "index.html", {'persons':persons})


def Contact_views(request):
    if request.method == "POST":
        ism = request.POST.get('ism')
        familya = request.POST.get('familya')
        yosh = request.POST.get('yosh')
        Person.objects.create(name=ism, last_name=familya, age=yosh)
        return redirect('index')
    return render(request, "contact.html")


def Delete_views(request, id):
    ism = Person.objects.get(id=id)
    ism.delete()
    return redirect('index')


def Edit_views(request, id):
    inson = Person.objects.get(id=id)
    if request.method == "POST":
        ism = request.POST.get('ism')
        familya = request.POST.get('familya')
        yosh = request.POST.get('yosh')
        inson.name = ism
        inson.last_name = familya
        inson.age = yosh
        inson.save()
        return redirect('index')
    return render(request, 'edit.html')