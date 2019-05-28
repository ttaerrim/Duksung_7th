from django.shortcuts import render

# Create your views here. 어떤 함수인지 간단히 주석 써주기
#후기 메인화면
def rmain(request):
    return render(request, 'rmain.html') 
#후기 글수정
def redit(request):
    return render(request, 'redit.html')
#후기 글쓰기
def rpost(request):
    return render(request, 'rpost.html')

