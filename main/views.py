from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Menfess
from .forms import MenfessEntryForm

# Create your views here.
def show_main(request):
    menfesses = Menfess.objects.all()

    context = {
        'menfesses': menfesses
    }

    return render(request, 'main.html', context)

def create_menfess_form(request):
    form = MenfessEntryForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, 'add/add.html', context)