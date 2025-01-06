from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .models import todo
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    if request.method == 'POST':
        task=request.POST.get('task')
        new_todo = todo(user=request.user,name = task)
        new_todo.save()


    all_todos = todo.objects.filter(user=request.user)
    context={
        'todos' : all_todos
    }    
    return render(request, 'todoapp/todo.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate password length
        if len(password) < 3:
            messages.error(request, 'Passwords must be at least 3 characters')
            return redirect('register')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'User Already Exists, Please Use a Different Username!')
            return redirect('register')

        # Create the new user
        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.save()
        messages.success(request, 'User Successfully Created! Login with your Registered Credentials.')
        
        # Redirect to avoid duplicate submission
        return redirect('login')

    return render(request, 'todoapp/register.html', {})


def LogoutView(request):
    logout(request)
    return redirect('loginpage')

def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')

        validate_user = authenticate(username=username,password=password)
        if validate_user is not None:
            login(request, validate_user)
            return redirect('home-page')

        else:
            messages.error(request,'Error user does not exists')
            return redirect('login')

    return render(request, 'todoapp/login.html', {})

@login_required
def deleteTask(request, name):
    # Use get_object_or_404 to handle the case where the object does not exist
    get_todo = get_object_or_404(todo, user=request.user, name=name)
    get_todo.delete()
    return redirect('home-page')
    


def Update(request,name):
    get_todo = get_object_or_404(todo, user=request.user, name=name)
    get_todo.status=True
    get_todo.save()
    return redirect('home-page')