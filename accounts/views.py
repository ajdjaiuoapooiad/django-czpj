from django.contrib import messages, auth

from django.shortcuts import redirect, render


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')




def register(request):
    return render(request,'accounts/register.html')

def logout(request):
    return render(request,'accounts/logout.html')

def dashboard(request):
    return render(request,'accounts/dashboard.html')