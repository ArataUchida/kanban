from django.contrib.auth import login # 追加
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm # 追加
from django.shortcuts import render, redirect # redirectをインポート


def index(request):
    return render(request, "kanban/index.html")

@login_required
def home(request):
    return render(request, "kanban/home.html")


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_instance = form.save()
            login(request, user_instance)
            return redirect("kanban:home")
    else:
        form = UserCreationForm()

    context = {
        "form": form
    }
    return render(request, 'kanban/signup.html', context)