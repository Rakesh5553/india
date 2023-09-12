from django.shortcuts import render
from testapp.models import *
from . import forms

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

def hydjobs1(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'testapp/hydjobs.html',context=my_dict)
    
#View function name and models class name should not be same
def blorejobs1(request):
    bjobs_list=blorejobs.objects.order_by('id')
    #print(bjobs_list)
    my_dict={'bjobs_list':bjobs_list}
    return render(request,'testapp/blorejobs.html',context=my_dict)


def punejobs1(request):
    form=forms.JobForm()
    return render(request,'testapp/punejobs.html',{'form':form})

def chennaijobs1(request):
    bjobs_list=blorejobs.objects.order_by('id')
    my_dict={'bjobs_list':bjobs_list}
    return render(request,'testapp/chennaijobs.html',context=my_dict)
