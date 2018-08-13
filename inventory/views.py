
from django.shortcuts import render,redirect
from inventory.forms import InventoryForm
from inventory.models import Inventory

def invReq(request):
    if request.method=="POST":
        form=InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/show')
    else:
        form=InventoryForm()
    return render(request,'index.html',{'form':form})

def show(request):
    inventory=Inventory.objects.all()
    return render(request,'show.html',{'inventory':inventory})

def edit(request,id):
    inventory=Inventory.objects.get(id=id)
    return render(request,'edit.html',{'inventory':inventory})

def update(request,id):
    inventory=Inventory.objects.get(id=id)
    form=InventoryForm(request.POST,instance=inventory)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{'inventory':inventory})

def delete(request,id):
    inventory=Inventory.objects.get(id=id)
    inventory.delete()
    return redirect("/show")

