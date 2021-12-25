from django.contrib.auth import login, authenticate
from .models import User,Gift
from Wallet.forms import TransferForm
from .forms import SignUpForm,GiftForm
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
    if not request.user.is_authenticated:
        return redirect('home')
    else:
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

def collectgift(request, id):
    if not request.user.is_authenticated:
        gift = Gift.objects.get(pk=id)
        fromusr = gift.from_usr
        fromusr.coins -= gift.ammount
        request.user.coins += gift.ammount
        request.user.gifts.remove(gift)
        fromusr.save()
        request.user.save()
        gift.delete()
        return redirect('home')
    else:
        return render(request, 'Welcome.html')

def givegift(request):
    if request.method == 'POST':
        form = GiftForm(request.POST)
        if form.is_valid():
            form.save()
            to = form.cleaned_data.get('to')
            amount = form.cleaned_data.get('amount')
            message = form.cleaned_data.get('message')
            gift = Gift(from_usr=request.user, amount=amount, message=message)
            gift.save()
            touser = User.objects.get(username=to)
            touser.gifts.add(gift)
            touser.save()
            return redirect('home')
    else:
        form = GiftForm()
    return render(request, 'gift.html', {'form': form})
