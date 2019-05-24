from django.shortcuts import render, get_object_or_404, redirect
from .models import apply
from .forms import ApplyForm
# Create your views here.

def addetail(request,apply_id):
    #applys = apply.objects #쿼리셋 #메소드
    apply_addeatil = get_object_or_404(Apply, pk = apply_id)
    return render(request,'addetail.html',{'applys': apply_addeatil})



# Create your views here.

# 지원하기
def form(request):
    if request.method == "POST":
        form = ApplyForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.save()
            return redirect('form')
    else:
        form = ApplyForm()
        return render(request, 'form.html', {'form':form})
def adview(request):
    applies = Apply.objects.all()
    return render(request, 'adview.html', {'applies' : applies})
