from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Register view
def register_view(request):
    # Save the form data if the form is valid
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list') 
    else:
        # UserCreationForm is a built-in form in Django
        form = UserCreationForm()
    
    # return the form to the template
    return render(request, 'users/register.html', {'form': form})
