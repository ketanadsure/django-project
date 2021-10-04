from django.shortcuts import render,redirect

from apps.forms import StudentForm
from django.contrib.auth.forms import UserCreationForm

from apps.models import Student

def welcome(request):
    return render(request,'welcome.html')


def show_student(request):
    data = Student.objects.all()
    return render(request,'show.html',{'data':data})

def add_student(request):
    form = StudentForm()
    print(request.POST)
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/show/")
    return render(request,'add.html',{'form':form})


def update_student(request,id):
    obj = Student.objects.get(pk = id)
    form = StudentForm(instance = obj)
    if request.method == "POST":
        form = StudentForm(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect("/show/")
    return render(request, 'update.html', {'form': form,'obj':obj})

def delete_student(request,id):
    obj = Student.objects.get(pk=id)
    obj.delete()
    return redirect("/show/")


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'register.html',{'form':form})