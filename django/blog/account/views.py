from django.shortcuts import render

from account import forms

def signup(request):
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = forms.RegisterForm()

    return render(request, 'account/signup.html', {'form': form})
