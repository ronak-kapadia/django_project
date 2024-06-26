from django.shortcuts import render
from django.http import HttpResponse
from .models import Department

def create_department(request):
    if request.method == 'POST':
      
        name = request.POST.get('name')
        role = request.POST.get('role')

        
        if name and role:
           
            department = Department.objects.create(
                name=name,
                role=role
            )
            return HttpResponse('Department Created')
        else:
            return HttpResponse('Name and Role are required')

    elif request.method == 'GET':
       
        departments = Department.objects.all()
        # for obj in departments:
        #     print(obj.name, obj.role)

        return render(request,'departments.html',{'departments': departments})




































































# from django.shortcuts import render,redirect
# from django.http import HttpResponse
# from django.template import loader
# from .models import Department
# from .forms import DepartmentForm


# def create_department(request):
#     if request.method == 'POST':        
#         data = request.POST

#         print(data)

#         name = data.get('name')
#         role = data.get('role')

#         department = Department.objects.create(
#             name=name,
#             role=role
#         )
        
#         print(department)

#         return HttpResponse('Deparment Created')
    
#     if request.method == 'GET':

#         departments = Department.objects.all()
#         for obj in departments:
#             print(obj.name, obj.role)

#         department = Department.objects.get(name='Ronak')
#         print(department.role, department.name)

#         departments = Department.objects.filter(role='Mobile')
#         for obj in departments:
#             print(obj.name, obj.role)


#         return HttpResponse('done')

# # def get_department(request):
    
        