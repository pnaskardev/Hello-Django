from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        # process form
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            form.save()
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})
