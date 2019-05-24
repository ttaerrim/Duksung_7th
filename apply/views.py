from django.shortcuts import render, get_object_or_404
from .models import apply
# Create your views here.

def addetail(request,apply_id):
    #applys = apply.objects #쿼리셋 #메소드
    apply_addeatil = get_object_or_404(Apply, pk = apply_id)
    return render(request,'addetail.html',{'applys': apply_addeatil})