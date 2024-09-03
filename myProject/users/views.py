from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Register view
def register_view(request):
    # Save the form data if the form is valid
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('posts:list') 
    else:
        # UserCreationForm is a built-in form in Django
        form = UserCreationForm()
    
    # return the form to the template
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #! Log the user in
            login(request, form.get_user())
            return redirect('posts:list') 
    else:
        form = AuthenticationForm()
        
    return render(request, 'users/login.html', {'form': form})
