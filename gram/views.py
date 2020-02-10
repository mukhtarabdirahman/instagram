from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .forms import UserCreateForm
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
            # return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'index.html')