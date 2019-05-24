from django.shortcuts import render

# Create your views here.
def rmain(request):
    return render(request, 'rmain.html')
    
def redit(request):
    return render(request, 'redit.html')

def rpost(request):
    return render(request, 'rpost.html')

