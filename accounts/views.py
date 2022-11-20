from django.shortcuts import render, redirect

from .forms import userForm

from .models import User

# Create your views here.


def register_user(request):
   
    if request.method == 'POST':
        form = userForm(request.POST)
        print(form.changed_data)
        if form.is_valid():
            passsword = form.cleaned_data['password']
            user = form.save(commit=False) #form ready to be save, but not yet saved
            user.set_password(passsword)
            user.role = User.CUSTOMER # assign role to this particular user
            user.save()
            return redirect('register-user')
      
    else:
        form = userForm()


    context = {
        'form' : form
    }
    return render(request, 'accounts/register-user.html', context)