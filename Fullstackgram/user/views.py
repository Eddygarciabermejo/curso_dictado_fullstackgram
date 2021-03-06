from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

#Exception
from django.db.utils import IntegrityError
#Models
from django.contrib.auth.models import User
from user.models import Profile

# Create your views here.
def login_views(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Wrong username or password'})
    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        password_confirmation = request.POST['passwd_confirmation']
        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        try:
            user = User.objects.create_user(username = username, password=password )
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username already exist'} )

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']

        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html' )