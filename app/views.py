from django.shortcuts import render,redirect
from django.views.generic import View
from app.forms import MobileDeviceForm
from app.models import MobileDevice

# Create your views here.

class MobileView(View):
    def get(self,request):
        form=MobileDeviceForm()
        return render(request,"mobile.html",{"form":form})
    def post(self,request):
        form = MobileDeviceForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Invalid Form")
        form=MobileDeviceForm(request.POST)
        return render(request,"mobile.html",{"form":form})


class MobileList(View):
    def get(self, request):
        qs = MobileDevice.objects.all()
        return render(request, "mobilelist.html", {"qs": qs})

    def post(self, request):
        text_value = request.POST.get("text")  
        qs = MobileDevice.objects.filter(brand__icontains=text_value) 
        
        return render(request, "mobilelist.html", {"qs": qs})


class Mobiledetails(View):
    def get(self,request,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=MobileDevice.objects.get(id=id)
        return render(request,"mobiledetails.html",{"qs":qs})
        
        
class Mobileremove(View):
    def get(self, request, **kwargs):
        id = kwargs.get("pk")
        qs = MobileDevice.objects.get(id=id).delete()
        
        return redirect('lst')
    
class Mobileupdate(View):
    def get(self,request,**kwargs):
        id=kwargs.get("pk")
        qs=MobileDevice.objects.get(id=id)
        form=MobileDeviceForm(instance=qs)
        return render(request,"mobileedit.html",{"form":form})
    
    def post(self,request,**kwargs):
        id=kwargs.get("pk")
        qs=MobileDevice.objects.get(id=id)
        form=MobileDeviceForm(request.POST,instance=qs)
        if form.is_valid:
            form.save()
        else:
            print("get out")
        return redirect('lst')
       