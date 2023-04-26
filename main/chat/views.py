from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Chat, Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from .forms import UserForm

def start(request): # представление стартовой страницы
    return render(request, 'start.html')

def log_user(request): # представление страницы авторизации
    if request.method == 'POST':
        user_name = request.POST.get('user-name')
        password = request.POST.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') # поользователь авторизуется и попадает на страницу со списоком чатов
    return render(request, 'chat/log-user.html')

def log_out(request): # представление выхода, перенаправляющее нас на стартовую страницу
    logout(request)
    return redirect('start')

def reg_user (request): # представление регистрации
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST) # заполнение формы
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            # регистрация после проверки данных
            return redirect('index') # пользователь регистрируется и попадает на страницу со списоком чатов
    return render(request, 'chat/reg-user.html', {'form' : form})

def password_change(request):  # представление смены пароля
    if request.method == 'POST':
        username = request.POST.get('username')
        user = User.objects.get(username=username)
        password = request.POST.get('password')
        user.set_password(password)
        user.save()
        login(request, user)
        return redirect('index')  # пользователь меняет пароль и попадает на страницу со списоком чатов
    return render(request, 'chat/change-password.html')


@login_required(login_url='log-in')
def index(request): # представление списка чатов
    req = request.GET.get('find')
    fix = Chat.objects.filter(fix = 1)
    chats = Chat.objects.filter(fix = 0)
    if req != None:
        if req[1:].isnumeric() and req[:1] == '#':
            find = int(req[1:])
            chats = Chat.objects.filter(id=find)
        else:
            find = request.GET.get('find')
            chats = Chat.objects.filter(name__icontains=find)
    else:
        find = ''
    context = {'chats':chats,
               'find':find,
               'fix':fix}
    return render(request, 'chat/index.html', context)

@login_required(login_url='log-in')
def chat(request, Id):
    chat_id = Chat.objects.get(id=Id)

    if request.method == 'POST':
        message = request.POST['message']

        print(message)

        new_message = Message(chat=chat_id, words=message, user=request.user)
        new_message.save()

    get_messages = Message.objects.filter(chat=chat_id)

    context = {
        "messages": get_messages,
        "user": request.user,
        "chat": chat_id,
    }
    return render(request, 'chat/chat.html', context)

@login_required(login_url='log-in')
def del_message(request, Id, id): #представление удаления сообщения
    message = Message.objects.get(id=Id)
    if request.method == 'POST':
        message.delete()
        return redirect('chat', id) # после удаления возвращает в чат
    return render(request, 'chat/del-message.html', {'message':message})


@login_required(login_url='log-in')
def chat_up(request, Id): #представление редактирования чата
    chat = Chat.objects.get(id=Id)

    if request.method == 'POST':
        chat.name = request.POST.get('name')
        chat.text = request.POST.get('text')
        chat.save()
        return redirect('index')

    return render(request, 'chat/create-chat.html')

@login_required(login_url='log-in')
def create_chat(request): #представление создания чата
    if request.method == 'POST':
        chat = Chat.objects.create(
            author = request.user,
            name = request.POST.get('name'),
            text = request.POST.get('text'),
            fix = 0
        )
        return redirect('index')
    return render(request, 'chat/create-chat.html')

@login_required(login_url='log-in')
def del_chat(request, Id): #представление удаления чата
    chat = Chat.objects.get(id=Id)
    if request.method == 'POST':
        chat.delete()
        return redirect('index')
    return render(request, 'chat/delete-chat.html', {'chat':chat})

@login_required(login_url='log-in')
def fix_chat(request, Id): #представление закрепления чата
    chat = Chat.objects.get(id=Id)
    if chat.fix == 0:
        msg = 'Закрепить'
    else:
        msg = 'Открепить'
    if request.method == 'POST':
        chat.fixed()
        chat.save()
        return redirect('index')
    return render(request, 'chat/fix-chat.html', {'chat':chat, 'msg':msg})

