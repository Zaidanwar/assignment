from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import *
from django.http import HttpResponse

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'homepage.html')
class Register1(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):

            data = request.POST
            email = data["email"]

            firstname = data["fullname"]

            password = data["pass"]
            dob=data["dob"]
            gender=data["gender"]
            r1=Register(email=email,fullname=firstname,password=password,dob=dob,gender=gender)
            r1.save()

            return redirect('/myapp/home/')



