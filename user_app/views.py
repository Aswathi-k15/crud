from django.shortcuts import render,redirect
from user_app.models import *
# Create your views here.
def user_registration(request):
    if request.method == "POST":
        names = request.POST.get("user_name")
        emails = request.POST.get("email")
        passwords = request.POST.get("password")
        phonenumbers = request.POST.get("phone_number")
        print(names, emails, passwords, phonenumbers)
        data = User()
        data.user_name = names
        data.email = emails
        data.password = passwords
        data.phone_number = phonenumbers
        data.save()
        return redirect('/')

    return render(request, 'user_register.html')
def view_users(request):
    user=User.objects.all()
    return render(request,'view_users.html',{'user':user})

def user_edit(request,user_id):
    if request.method == "POST":
        names = request.POST.get("user_name")
        emails = request.POST.get("email")
        passwords = request.POST.get("password")
        phonenumbers = request.POST.get("phone_number")
        print(names, emails, passwords, phonenumbers)
        data = User.objects.get(user_id=user_id)
        data.user_name = names
        data.email = emails
        data.password = passwords
        data.phone_number = phonenumbers
        data.save()
        return redirect('/')
    user=User.objects.filter(user_id=user_id)

    return render(request, 'user_update.html',{'user':user})

def remove(request, user_id):
    data = User.objects.get(user_id=user_id)
    data.delete()
    return redirect('/')