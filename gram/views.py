from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .forms import UserCreateForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def gram_of_day(request):
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    return render(request, 'base.html')

def home (request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'index.html', {'form': form})
@login_required(login_url='/accounts/login/')
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('signup_success.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "login.html",
                    context={"form":form})