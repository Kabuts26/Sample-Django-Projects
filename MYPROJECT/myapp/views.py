from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name' : 'Clive',
        'age' : 22,
        'nationality' : 'Philippines'
    }
    return render(request, 'index.html', context)
