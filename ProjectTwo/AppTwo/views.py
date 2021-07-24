from django import contrib
from django.shortcuts import render
from AppTwo.forms import myNewUser

# Create your views here.

def index(request):

    return render(request,'second_app/index.html')

def users(request):

    form=myNewUser()

    if request.method =='POST':

        form =myNewUser(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Invalid Form")

    return render(request,'second_app/user.html',{'form' : form }) 