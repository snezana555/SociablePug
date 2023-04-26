from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from django.core.files.storage import FileSystemStorage
from .forms import PostForm

@login_required(login_url='log-in')
def posts(request): #представление страницы со списком постов
    req = request.GET.get('find')
    posts = Post.objects.filter()
    if req != None:
        if req[1:].isnumeric() and req[:1] == '#':
            find = int(req[1:])
            posts = Post.objects.filter(id=find)
        else:
            find = request.GET.get('find')
            posts = Post.objects.filter(name__icontains=find)
    else:
        find = ''
    context = {'posts':posts,
               'find':find}
    return render(request, 'post/posts.html', context)

@login_required(login_url='log-in')
def post(request, Id):
    post_id = Post.objects.get(id=Id)

    if request.method == 'POST':
        comment = request.POST['comment']
        new_comment = Comment(post=post_id, words=comment, user=request.user)
        new_comment.save()

    get_comments = Comment.objects.filter(post=post_id)

    context = {
        "comments": get_comments,
        "user": request.user,
        "post": post_id,
    }
    return render(request, 'post/comments.html', context)

@login_required(login_url='log-in')
def del_comment(request, Id, id): #представление страницы с удалением комментария
    comment = Comment.objects.get(id=Id)
    if request.method == 'POST':
        comment.delete()
        return redirect('post-comments', id)
    return render(request, 'post/post-comments.html', {'comment':comment})


@login_required(login_url='log-in')
def post_up(request, Id): # представление редактирования поста
    post = Post.objects.get(id=Id)

    if request.method == 'POST':

        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        if request.FILES:
            file = request.FILES['file']
            fs = FileSystemStorage(location = "static/image-user/{0}/".format(post.title))
            filename = fs.save(file.name, file)
            post.filename = file.name
            post.url_file = fs.path(file.name)
            post.save()
        return redirect('posts')

    return render(request, 'post/create-post.html')

@login_required(login_url='log-in')
def create_post(request): #представление для страницы редактирования поста
    if request.method == 'POST':
        post = Post.objects.create(
            author_post = request.user,
            title = request.POST.get('title'),
            content = request.POST.get('content'),
        )
        if request.FILES:
            file = request.FILES['file']
            fs = FileSystemStorage(location = "static/image-user/{0}/".format(post.title))
            filename = fs.save(file.name, file)
            post.filename = file.name
            post.url_file = fs.path(file.name)
            post.save()
        return redirect('posts')
    return render(request, 'post/create-post.html')

@login_required(login_url='log-in')
def del_post(request, Id): # представление для удаления поста
    post = Post.objects.get(id=Id)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'post/delete-post.html', {'post':post})




