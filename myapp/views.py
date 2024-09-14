
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .middlewares import auth


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  # Login the user here
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# @auth
def logout(request):
    auth_logout(request)
    return redirect('login')

# @auth
@login_required
def dashboard(request):
    user = request.user  # This retrieves the logged-in user's details
    context = {
        'username': user.username  # Get the username of the logged-in user
    }
    return render(request, 'dashboard.html', context)

# @auth
@login_required
def videocall(request):
    return render(request, 'videocall.html',{'name':request.user.username})


# @login_required
# def joinroom(request):
#     if request.method=='POST':
#         # roomID=request.POST['roomID']
#         roomID=request.POST.get('roomID')
#         return redirect('/meeting?roomID='+roomID)
#     # return render(request, 'joinroom.html',{'name':request.user.username})
#     return render(request, 'joinroom.html',{'roomID':roomID})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def joinroom(request):
    if request.method == 'POST':
        roomID = request.POST.get('roomID')
        if roomID:  # Check if roomID is provided
            return redirect(f'/video-call?roomID={roomID}')
        else:
            # Handle the case where roomID is not provided
            return render(request, 'videocall.html', {'error': 'Room ID is required.'})
    else:
        # Handle GET request or other methods
        return render(request, 'joinroom.html')


@login_required
# @auth
def meeting(request):
    roomID = request.GET.get('roomID')
    context = {'roomID': roomID}
    return render(request, 'meeting.html', context)



def home(request):
    return render(request,'home.html')