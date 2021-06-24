from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def home(r):
    data={"biz":Biz.objects.all(),"cat":Category.objects.all()}
    return render(r,"home.html",data)


def add(r):
    if r.method=="POST":
        form=BizForm(r.POST, r.FILES)
        if form.is_valid():
            form.save()
        return redirect(home)
    data={"form":BizForm}
    return render(r,"insert.html",data)

def search(r):
    if r.method=="GET":
        search=r.GET.get('search')
        data = {"biz":Biz.objects.filter(title__icontains=search),"cat":Category.objects.all()}
    return render(r,'cat.html',data)




def biz(r,slug):
    data={"biz":Biz.objects.filter(slug=slug),"cat":Category.objects.all()}
    return render(r,'biz.html',data)


def category(r,cat_id):
    data={"biz":Biz.objects.filter(category=cat_id),"cat":Category.objects.all()}
    return render(r,'cat.html',data)


