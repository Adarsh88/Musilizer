from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from musilizerapp.models import Entry
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.http import HttpResponse
# Imaginary function to handle an uploaded file.


def home(request):
    return render(request, 'musilizer/home.html')

def index(request):
    return render(request,'musilizer/index.html')
    
def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'musilizer/register.html', context)


def upload(request):
    return render(request, 'musilizer/upload.html')

def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+ user+'!')

            return redirect('/login')

    context = {'form':form}
    return render(request, 'musilizer/register.html', context)

def loginPage(request):

    if request.method == "POST":
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')

        user = authenticate(request, username=username1, password=password1)

        if user is not None:
            return redirect('home')
        else:
            messages.info(request, 'Username OR Password is incorrect!')

    context = {}
    return render(request, 'musilizer/login.html', context)    

def success(request):
    if request.method != "POST":
        return HttpResponseRedirect('/')

    try:
        song_name = request.POST['song_name']
        file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name,file)
        uploaded_file_url = fs.url(filename)
        print("The song name is: " + filename)

        E = Entry.objects.create(unique_number=0,set_to_expire="n",file_name=song_name, audio_file=file)
        song_id = E.id
        print("The song id is: " + str(song_id))
        return render(request, 'musilizer/success.html', {'song_id': song_id})
    except:
        return HttpResponseRedirect('/error')


def retrieve(request):
    return render(request, 'musilizer/retrieve.html')

def play(request):
    if request.method != "POST":
        return HttpResponseRedirect('/')

    try:
        code_number = request.POST['code_number']

        print("The code number is " + code_number)

        song_entry = list(Entry.objects.filter(id=code_number))
        print(song_entry)

        return render(request, 'musilizer/play.html', {'song_entry': song_entry})
    except:
        #return HttpResponseRedirect('/error')
        return render(request, 'musilizerplay.html', {'song_entry': song_entry})


def error(request):
    return render(request, 'musilizer/error.html')