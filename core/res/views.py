from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.
from .models import Contact
from django.http import HttpResponse


def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('completed')
    return render(request,'index.html',{'form':form})

def post(request):
    return render(request,'resume_screener.html')

def chat(request):
    return render(request,'chatForum.html')

def completed(request):
    data=Contact.objects.all()
    context2={
        'data': data
    }
    return render(request,'completed.html',context2)

def right(request):
    return render(request,'website_design.html')