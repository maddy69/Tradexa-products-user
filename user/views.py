from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
def home(request):

    if request.method == 'POST':
        first_name = request.POST('First Name')
        last_name = request.POST('Last Name')
        email = request.POST('email')
        Password = request.POST('Password')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, Password=Password)
        user.save();
        print('user created')
        return redirect('/')
    else:
        return render(request , 'index.html')
