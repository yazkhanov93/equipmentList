import os
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.conf import settings
from django.http import HttpResponse, Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *


# function for download equipmentlist file or image
@login_required(login_url="login")
def download(request, pk): 
    f = EquipmentList.objects.get(id=pk)
    userId = request.user.id
    f.userDownloadId.add(userId)
    path = f.fileImage.path
    file_path = os.path.join(settings.BASE_DIR, str(path))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read())
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404


# function for add equipmentList
@login_required(login_url="login")
def addEquipmentList(request):
    form = EquipmentListForm()
    if request.method == "POST":
        form = EquipmentListForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "equipmentList.html", {"form":form,"sp":Specification.objects.all()})


#function for edit equipmentList
@login_required(login_url="login")
def editEquipmentList(request, pk):
    eq_list = EquipmentList.objects.get(id=pk)
    if request.method == "POST":
        form = EquipmentListForm(request.POST, request.FILES, instance=eq_list)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "equipmentList.html", {"form":EquipmentListForm(instance=eq_list), "sp":Specification.objects.all()})


#function for delete equipmentList
@login_required(login_url="login")
def deleteEquipmentList(request, pk):
    eq_list = EquipmentList.objects.get(id=pk)
    eq_list.delete()
    return redirect("index")


#function for filter equipmentlist for specification
@login_required(login_url="login")
def specification(request, pk):
    eq_list = EquipmentList.objects.filter(specificationId=pk)
    search = request.GET.get("search", "")
    if search:
        eq_list = eq_list.filter(Q(equipmentId__title__icontains=search))
    return render(request, "specification.html", {"eq_list":eq_list, "sp":Specification.objects.all()})


#home page
@login_required(login_url="login")
def index(request):
    sp = Specification.objects.all()
    eq_list = EquipmentList.objects.filter(specificationId=sp.first()) 
    search = request.GET.get("search", "")
    if search:
        eq_list = eq_list.filter(Q(equipmentId__title__icontains=search))
    return render(request, "index.html", {"eq":eq_list, "sp":sp})


#login
def logIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
    return render(request, "login.html", {})


#logut
def logOut(request):
    logout(request)
    return redirect("login")