from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User  
from django.contrib import messages
from django.contrib.auth import logout as auth_logout



# LOGIN VIEW
def login(request):
    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        username_val = request.POST.get('username')
        password_val = request.POST.get('password')
        
        user = authenticate(username=username_val, password=password_val)
        
        if user is None and '@' in username_val:
            try:
                user_obj = User.objects.get(email=username_val)
                user = authenticate(username=user_obj.username, password=password_val)
            except User.DoesNotExist:
                user = None

        if user is not None:
            auth_login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('youthclub')
        else:
            messages.error(request, "Invalid credentials.")
            return render(request, 'login.html')
            
    return render(request, 'login.html')


# SIGNUP VIEW (Renamed to match your layout perfectly)
def signup(request):
    if request.user.is_authenticated:
        return redirect('Home')

    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'Signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'Signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return render(request, 'Signup.html')

        first_name, *last_name = full_name.split(' ', 1)
        last_name = last_name[0] if last_name else ""

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.save()

        auth_login(request, user)
        messages.success(request, f"Welcome to Nachiketa Foundation, {first_name}!")
        return redirect('Home')

    return render(request, 'Signup.html')

def logout_view(request):
    auth_logout(request)  # 1. Safely destroys the active session keys and clears cookies
    messages.info(request, "You have been securely logged out.")  # 2. Sets a flash notification message
    return redirect('login')  # 3. Sends the user straight back to the login screen
