from django.shortcuts import render
from .forms import ReviewForm
from .models import Review

# Create your views here.
def rmain(request):
    return render(request, 'rmain.html')
    
def rpost(request):
    if request.method == "RPOST":
        form = ReviewForm(request.RPOST)
        if form.is_valid():
            review = form.save(commit = False)
            reveiw.save()
            return redirect('rshow') 
    else:
        form = ReviewForm()
        return render(request, 'rpost.html', {'form':form})

def redit(request):
    review = get_object_or_404(Reveiw, pk=pk)
    if request.method == "RPOST":
        form = ReviewForm(request.RPOST, instance=review)
        if form.is_valid():
            review = form.save(commit = False)
            reveiw.save()
            return redirect('rshow') 
    else:
        form = ReviewForm(instance=review)
        return render(request, 'rpost.html', {'form':form})