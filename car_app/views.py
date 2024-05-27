from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Car
from django.views import View


class CarCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'car_app/create_user.html')

    def post(self, request, *args, **kwargs):
        model=request.POST["model"]
        body_style=request.POST["style"]
        fuel_type=request.POST["fuel"]
        seating_capacity=request.POST["seating"]
        transmission_type=request.POST["transmission"]
        price_per_hour=request.POST["price"]
        profile_pic=request.FILES["profile"]
        obj=Car(model=model,body_style=body_style,fuel_type=fuel_type,seating_capacity=seating_capacity,transmission_type=transmission_type,price_per_hour=price_per_hour,profile_pic=profile_pic)
        obj.save()
        return render( request,"car_app/create_user.html")


class CarListView(View):
    def get(self, request, *args, **kwargs):
        queryset=Car.objects.all()
        # queryset=Car.objects.get(id=1)
        return render(request, "car_app/list_user.html",{'post':queryset})

class CarUpdateView(View):
    def post(self, request, *args, **kwargs):
        obj=Car.objects.get(pk=id)
        model=request.POST["model"]
        body_style=request.POST["style"]
        fuel_type=request.POST["fuel"]
        seating_capacity=request.POST["seating"]
        transmission_type=request.POST["transmission"]
        price_per_hour=request.POST["price"]
        profile_pic=request.FILES["profile"]

        obj.model=model
        obj.body_style=body_style
        obj.fuel_type=fuel_type
        obj.seating_capacity=seating_capacity
        obj.transmission_type=transmission_type
        obj.price_per_hour=price_per_hour
        obj.profile_pic=profile_pic
        obj.save()
        return redirect ("/list-user/")
    def get(self, request, *args, **kwargs):
        id=self.kwargs['id']
        obj=Car.objects.get(pk=id)
        return render (request,"car_app/update_user.html",{'post':obj})

def delete_user(request,id):
    obj=Car.objects.get(pk=id)
    obj.delete()
    return redirect("/")

def details_user(request,id):
    obj=Car.objects.get(pk=id) 
    return render(request, "car_app/details_user.html",{"post":obj})



