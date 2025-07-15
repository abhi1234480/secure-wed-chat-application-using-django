from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm

def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('rooms')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})
