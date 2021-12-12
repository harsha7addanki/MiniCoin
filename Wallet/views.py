from django.contrib.auth import login, authenticate
from .models import User
from Wallet.forms import TransferForm
from .forms import SignUpForm
from django.shortcuts import render, redirect

# Create your views here.
def viewWallet(request):
    if not request.user.is_authenticated:
        return render(request, 'Welcome.html')
    else:
        return render(request, 'viewwallet.html',{"user":request.user})
    

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def transfer(request):
    if request.method == 'POST':
        form = TransferForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data.get('to')
            ammount = form.cleaned_data.get('amount')
            print(ammount)
            fromuser = request.user
            if fromuser.coins < int(ammount):
                return redirect('home')
            touser = User.objects.get(username=to)
            fromuser.coins -= ammount
            touser.coins += ammount
            fromuser.save()
            touser.save()
            return redirect('home')
    else:
        form = TransferForm()
    return render(request, 'transfer.html', {'form': form})

def userpage(request):
    ...