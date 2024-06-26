from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Office

def office(request):
    template=loader.get_template('office.html')
    return HttpResponse(template.render())

def create_office(request):
    if request.method =='POST' :
        data= request.POST 

        print(data)

        location = data.get('location')
        building = data.get('building')

        office=Office.objects.create(
            location = location,
            building = building 
        )

        print(office)

        return HttpResponse ('Office Created ')
    
    if request.method =='GET' :

        offices = Office.objects.all()
        for obj in offices :
            print(obj.location,obj.building)

        # office =Office.objects.get(location='Lower Parel')
        # print(office.location,office.building)

        offices =Office.objects.filter(building='Business Arcade')
        for obj in offices:
            print(obj.location,obj.role)

        return HttpResponse ('Done')



