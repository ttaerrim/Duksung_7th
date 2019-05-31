from django.shortcuts import render,get_object_or_404,redirect
from .forms import BoardForm, CommentForm
from .models import Board, Comment
from django.utils import timezone
# Create your views here.

def post(request):
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit = False)
            board.update_date =timezone.now()
            board.save()
            return redirect('show')
    else:
        form = BoardForm()
        return render(request,'post.html',{'form':form})    

def show(request):
    boards = Board.objects
    return render(request, 'show.html', {'boards':boards})

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
    

def edit(request, pk):
    board = get_object_or_404(Board, pk=pk)  
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board) 
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

# def comment_edit(request, board_pk, pk):
#     comment = get_object_or_404(pk=pk)

#     if request.method == 'POST':
#             comment_form = CommentForm(request.POST, instance=comment)

#             if comment_form.is_valid():
#                     comment = comment_form.save(commit=False)
#                     comment.board = Board.objects.get(pk=board_pk)
#                     comment.save()
#                     return redirect('detail', comment.board.pk)
#                     #return redirect('detail', board_pk)

#     else:
#             comment_form = CommentForm(instance=comment)
#     return render(request, 'comment_form.html', {'comment_form' : comment_form})   