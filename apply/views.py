from django.shortcuts import render
from .forms import ApplyForm
from .models import Apply

# Create your views here.
def adview(request):
    applies = Apply.objects.all()
    return render(request, 'adview.html', {'applies' : applies})