from django.shortcuts import render,get_object_or_404,redirect
from .forms import BoardForm, CommentForm
from .models import Board, Comment
from django.utils import timezone


# Create your views here.
from django.core.paginator import Paginator


def post(request):
    if request.method == "POST":
        form = BoardForm(request.POST,request.FILES)
        if form.is_valid():
            board = form.save(commit = False)
            board.update_date =timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm()
        return render(request,'post.html',{'form':form})    

def show(request):
    board = Board.objects
    boards = Board.objects.all().order_by('-id')
    paginator = Paginator(boards, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'show.html', {'boards':boards, 'posts':posts})

def detail(request,board_id):
    board_detail = get_object_or_404(Board, pk=board_id)
    comments = Comment.objects.filter(board_id=board_id)
    context = {
            'board' : board_detail,
            'comments' : comments
    }
    return render(request,'detail.html',context )


def comment_write(request, pk):

    if request.method == 'POST':
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.board = Board.objects.get(pk=pk)
                    comment.created_at = timezone.now()
                    comment.save()
                    return redirect('detail', pk)
    else:
            comment_form = CommentForm()
    return render(request, 'comment_form.html', {'comment_form' : comment_form})
    
def comment_edit(request, board_pk, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
            comment_form = CommentForm(request.POST, instance=comment)

            if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.board = Board.objects.get(pk=board_pk)
                    comment.save()
                    return redirect('detail', board_pk)

    else:
            comment_form = CommentForm(instance=comment)
    return render(request, 'comment_form.html', {'comment_form' : comment_form})   
    
def edit(request, pk):
    board = get_object_or_404(Board, pk=pk)  
    if request.method == "POST":
        form = BoardForm(request.POST,request.FILES,instance=board)
        if form.is_valid():
            board = form.save(commit = False)
            board.update_date=timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm(instance=board)
    return render(request,'edit.html',{'form':form})

def delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('show')

 

# @login_required
# @require_POST
# def like(request):
#     pk = request.Board.get('pk', None)
#     post = get_object_or_404(Board, pk=pk)
#     post_like, post_like_created = post.like_set.get_or_create(user=request.user)

#     if not post_like_created:
#         post_like.delete()
#         message = "좋아요 취소"
#     else:
#         message = "좋아요"

#     context = {'like_count': post.like_count,
#                'message': message,
#                'nickname': request.user.profile.nickname}

#     return HttpResponse(json.dumps(context), content_type="application/json")
