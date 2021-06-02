from django.shortcuts import render,redirect
from todosapp.forms import  TodoCreateForm,TodoUpdateForm,UserRegisterationForm,LoginForm
from .models import  todo as Todos
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_required(func):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("loginview")
        else:
            return func(request,*args,**kwargs)
    return wrapper

def create_todo(request,*args,**kwargs):
    context={}
    form=TodoCreateForm(initial={"user":request.user})
    context["form"]=form
    if request.method=="POST":
        form=TodoCreateForm(request.POST)
        if form.is_valid():
            taskname=form.cleaned_data.get("task_name")
            status=form.cleaned_data.get("status")
            username=form.cleaned_data.get("user")
            todo=Todos(taskname=taskname,status=status,user=username)
            todo.save()
            print("saved")
        return redirect("alltodos")
    return render(request,"todo/createtodo.html",context)

@login_required
def listalltodos(request,*args,**kwargs):
    todos=Todos.objects.filter(user=request.user)
    context={}
    context["todo"]=todos
    return render(request,"todo/listalltodos.html",context)

@login_required
def delete_todo(request,*args,**kwargs):
    id=kwargs.get("id")
    todos=Todos.objects.get(id=id)
    todos.delete()
    return redirect("alltodos")

@login_required
def update_todo(request,*args,**kwargs):
    id = kwargs.get("id")
    Todo=Todos.objects.get(id=id)
    form=TodoUpdateForm(instance=Todo)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=TodoUpdateForm(instance=Todo,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("alltodos")
    return render(request,"todo/update.html",context)

def Registration(request):
    form=UserRegisterationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginview")
        else:
            context["form"]=form
            return render(request,"todo/registeration.html",context)
    return render(request,"todo/registeration.html",context)

def login_todo(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return render(request,"todo/home.html")
            else:
                context["form"]=form
                return render(request,"todo/login.html",context)


    return render(request,"todo/login.html",context)

def django_logout(request):
    logout(request)
    return redirect("loginview")

