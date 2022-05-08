from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
from django.http import HttpResponse
from .models import Contact


def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'index.html',context)

def post(request):
    return render(request,'post.html')

def chat(request):
    return render(request,'chatForum.html')
def completed(request):
    data=Contact.objects.all()
    context={
        'data': data
    }
    return render(request,'completed.html',context)
def right(request):
    return render(request,'right.html')