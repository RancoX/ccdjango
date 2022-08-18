from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    # register a new user
    if request.method=='GET':
        # display blank user form
        form=UserCreationForm()
    else:
        # process filled form
        form=UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user=form.save()
            # log the current new user in and redirect to home page
            login(request,new_user)
            return redirect('learning_logs:index')

    # display a blank or invalid form
    context={'form':form}
    return render(request, 'registration/register.html', context)