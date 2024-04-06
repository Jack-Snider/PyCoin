from django.shortcuts import render, redirect

# Create your views here.
def index(request):

    # Get user info from request
    user = request.user

    # Check if user is logged in
    is_authenticated = user.is_authenticated

    print(f'user : {user}')
    print(f'is_authenticated : {is_authenticated}')

    # if user is not logged in, redirect the URL to /user/login
    if not is_authenticated:
        return redirect("/users/login")

    # When you write URL address for html file
    # You have to start from right under the templates folder
    # if common folder is under the templates folder
    # address will be like common/index.html
    return render(request, "common/index.html")