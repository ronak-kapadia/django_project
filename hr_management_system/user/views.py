from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def user(request):
    template=loader.get_template('registration.html')
    return HttpResponse(template.render())

def create_user(request) :
    if request.method=='POST' :
        form = UserForm(request.POST)

        if form.is_valid() :
            form.save()
            return HttpResponse("User is created successfully")
        
    else :
        form=UserForm()

    context= {
        'form':form,
    }

    return render(request,'registration.html',context)
