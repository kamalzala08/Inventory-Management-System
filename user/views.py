from django.shortcuts import render , redirect

from django.contrib.auth.forms import UserCreationForm 
from .forms import CreateUserForm , UserUpdateForm , ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def signin(request):
    return render(request, 'user/signin.html')

def signup(request): 
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # group = Group.objects.get(name='Customers')
            # user.groups.add(group)
            return redirect('signin')
    else:
        form = CreateUserForm()
    return render(request, 'user/signup.html',{'form':form})

@login_required
def logout(request):
    return render(request, 'user/logout.html')

@login_required
def profile(request):
    return render(request, 'user/profile.html')

@login_required
def updateprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    
    return render(request, 'user/update_profile.html',context)


 