from django.shortcuts import render, redirect, get_object_or_404
from .forms import PasteForm
from .models import Paste
from datetime import datetime, timedelta
from django.utils import timezone
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def create_paste(request):
    if request.method == 'POST':
        form = PasteForm(request.POST, request.FILES)
        if form.is_valid():
            paste = form.save(commit=False)
            expiration_time_minutes = int(form.cleaned_data['expiration_time'])
            paste.expiration_time = expiration_time_minutes
            paste.created_at = datetime.now()
            if form.cleaned_data['password']:
                paste.set_password(form.cleaned_data['password'])
            paste.save()
            return redirect('show_code', code=paste.code)
    else:
        form = PasteForm()
    return render(request, 'create_paste.html', {'form': form})

def show_code(request, code):
    return render(request, 'show_code.html', {'code': code})


def retrieve_paste(request, code):
    paste = get_object_or_404(Paste, code=code)
    
    if paste.is_expired():
        paste.is_active = False
        paste.save()
        return render(request, 'retrieve_paste.html', {'paste': None, 'error': 'The code has expired.'})

    if request.method == 'POST':
        password = request.POST.get('password')
        if paste.password:
            if paste.check_password(password):
                return render(request, 'retrieve_paste.html', {'paste': paste})
            else:
                return render(request, 'retrieve_paste.html', {'paste': None, 'error': 'The password is wrong.'})
        else:
            return render(request, 'retrieve_paste.html', {'paste': paste})

    return render(request, 'retrieve_paste.html', {'paste': paste, 'password_required': paste.password is not None})



def search_paste(request):
    code = request.GET.get('code')
    if code:
        return redirect('retrieve_paste', code=code)
    else:
        return redirect('home')
