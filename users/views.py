from django.shortcuts import render, redirect
from users.forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login, logout

# Choi
# Create your views here.
def login_view(request):

    # if user is logged in, redirect URL to /
    if request.user.is_authenticated:
        return redirect("")
    
    if request.method == "POST":
        form = LoginForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username = username, password = password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None, 'Given ID or Password is not valid.')
        context = {"form" : form}
        return render(request, "users/login.html", context)
    else:
        form = LoginForm()
        context = {"form" : form}
        return render(request, "users/login.html", context)
    
def logout_view(request):
    logout(request)
    return redirect("/users/login")
    

def signup(request):

    # Create SignupForm instance
    form = SignupForm()
    context = {"form" : form}

    return render(request, "users/signup.html", context)