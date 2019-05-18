from django.shortcuts import render,get_object_or_404,redirect
from .forms import TipForm
from .models import Tip
from django.utils import timezone
from django.http import HttpResponseRedirect,Http404,HttpResponse
import os
# Create your views here.
def post(request):
    if request.method=="POST":
        form=TipForm(request.POST,request.FILES)
        if form.is_valid():
            tip=form.save(commit=False)
            tip.update_date=timezone.now()
            tip.save()
            return HttpResponseRedirect('/tip/show/')

    else:
        form=TipForm()
        return render(request,'post.html',{'form':form})


def show(request):
    tips=Tip.objects.order_by('-id')
    return render(request,'show.html',{'tips':tips})


def detail(request,tip_id):
    tip_detail=get_object_or_404(Tip,pk=tip_id)

    return render(request,'detail.html',{'tip':tip_detail})


def edit(request,pk):
    tip=get_object_or_404(Tip,pk=pk)
    if request.method=="POST":
        form=TipForm(request.POST,request.FILES,instance=tip)
        if form.is_valid():
            tip=form.save(commit=False)
            tip.update_date=timezone.now()
            tip.save()
            return redirect('/tip/show/')

    else:
        form=TipForm(instance=tip)
        return render(request,'edit.html',{'form':form})


def delete(request,pk):
    tip=Tip.objects.get(id=pk)
    tip.delete()
    return redirect('show')

def deleteall(request):
    tips=Tip.objects.all()
    for tip in tips:
        tip.delete()
    return render(request,'show.html',{'tips':tips})



def download(request,pk):
    
    upload=get_object_or_404(Tip,pk=pk)
    file_url=upload.file.url[1:]
    if os.path.exists(file_url):
        with open(file_url,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/octet-stream")
            response['Content-Disposition']='inline:filename='+os.path.basename(file_url)
            return response
        raise Http404   

