from django.shortcuts import render, redirect
from .models import Student

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        roll = request.POST['roll']
        dept = request.POST['dept']
        sem = request.POST['sem']

        student = Student.objects.create(name=name, dept=dept, sem=sem, roll="cs-"+roll)
        student.save()
        data = Student.objects.all()

        return render(request, 'index.html', {'data': data})

    data = Student.objects.all()
    return render(request, 'index.html', {'data': data})

def delete(request, id):
    record = Student.objects.get(pk=id)
    record.delete()

    return redirect('index')

def update(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        roll = request.POST['roll']
        dept = request.POST['dept']
        sem = request.POST['sem']

        student = Student.objects.get(pk=id)
        student.name = name
        student.dept = dept
        student.sem = sem
        student.roll = roll
        student.save()

        return redirect('index')

    record = Student.objects.get(pk=id)
    return render(request, 'update.html', {'student': record})