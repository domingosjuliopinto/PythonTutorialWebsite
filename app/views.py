from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .form import ContactForm
from .qform import QuizForm
from app import globals

import re

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST.get('passwd')
        user = authenticate(username=username, password=password)
        print(user)
        print(username)
        print(password)
        if user is not None:
            print("Authenticated")
            login(request, user)
            return redirect('home')
        else:
            print("not authenticated")
            return render(request, 'app/index.html')
    return render(request, 'app/index.html')


def registration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST.get('password')
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
      
        # compiling regex
        pat = re.compile(reg)
        
        # searching regex                 
        mat = re.search(pat, password)
        
        # validating conditions
        if mat:
            print("Password is valid.")
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('/')
        else:
            messages.error(request, 'Invalid password!!')
            print("Password invalid !!")
            return render(request, 'app/signup.html')

    return render(request, 'app/signup.html')

def index(request):
    return render(request, 'homepage.html')

def pylessons(request):
    return render(request, 'pylessonspage.html')

def about(request):
    return render(request, 'aboutpage.html')

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('/home')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def pyquiz(request):
    if request.method == 'POST':
        qform = QuizForm(request.POST)
        if qform.is_valid():
            if globals.t == 5:
                return redirect('/full')
            if globals.t == 4:
                return redirect('/eighty')
            if globals.t == 3:
                return redirect('/sixty')
            if globals.t == 2:
                return redirect('/forty')
            if globals.t == 1:
                return redirect('/twenty')
            if globals.t == 0:
                return redirect('/zero')
    else:
        qform = QuizForm()
    return render(request, 'quiz.html', {'qform': qform})

#for beginner's page
def varandtc(request):
    return render(request, 'b-vatc.html')

def datatype(request):
    return render(request, 'b-daty.html')

def operation(request):
    return render(request, 'b-oper.html')

def strings(request):
    return render(request, 'b-string.html')

def lists(request):
    return render(request, 'b-list.html')

def tuples(request):
    return render(request, 'b-tupl.html')

def diction(request):
    return render(request, 'b-dict.html')

def sets(request):
    return render(request, 'b-sets.html')

def loops(request):
    return render(request, 'b-loops.html')

#for intermediate's page
def clasobj(request):
    return render(request, 'i-clob.html')

def filehand(request):
    return render(request, 'i-fiha.html')

def gui(request):
    return render(request, 'i-gui.html')

def inherit(request):
    return render(request, 'i-inhe.html')

def modules(request):
    return render(request, 'i-modu.html')

def polymor(request):
    return render(request, 'i-poly.html')

#afterquiz
def full(request):
    return render(request, 'result/full.html')

def eighty(request):
    return render(request, 'result/eighty.html')

def sixty(request):
    return render(request, 'result/sixty.html')

def forty(request):
    return render(request, 'result/forty.html')

def twenty(request):
    return render(request, 'result/twenty.html')

def zero(request):
    return render(request, 'result/zero.html')