from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Device

def device(request):
    template=loader.get_template('devices.html')
    return HttpResponse(template.render())

def create_device(request):
    if request.method=='POST' :
        data=request.POST

        print(data)

        name = data.get('name')
        type = data.get('type')


        device=Device.objects.create(
            name = name ,
            type = type 
        )

        print(office)

        return HttpResponse('Device Created')
    
    if request.method=='GET' :

        devices =  Device.objects.all()
        for obj in devices :
            print(obj.location,obj.type)


        devices= Device,objects.filter(name='apple')
        for obj in devices :
            print(obj.name,obj.type)

        return HttpResponse ('Done')