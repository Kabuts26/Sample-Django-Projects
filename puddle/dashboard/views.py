from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from item.models import Item
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    
    return render(request, 'dashboard/index.html', {
        'items': items,
    })

    
def logout_view(request):
    logout(request)
    return redirect('core:index')