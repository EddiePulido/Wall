from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    if 'id' in request.session:
        return redirect("/wall")
    return render(request,"wall_app/index.html")

def create(request):
    errors = User.objects.registration_validator(request.POST)

    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        # redirect the user back to the form to fix the errors
        return redirect('/')

    hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],password=hash1)

    request.session['id'] = user.id
    request.session['first_name'] = user.first_name


    return redirect("/wall")

def login(request):
    errors = User.objects.login_validator(request.POST)
    print(errors)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)

        return redirect("/")

    user = User.objects.get(email=request.POST['email'])
    request.session['id'] = user.id
    request.session['first_name'] = user.first_name



    return redirect("/wall")



def logout(request):
    request.session.flush()

    return redirect("/")

def wall(request):
    context = {
        "messages" : Message.objects.all().order_by("-created_at"),
    }

    return render(request,"wall_app/wall.html",context)


def post_message(request):
    user = User.objects.get(id=request.session['id'])
    M = Message.objects.create(message = request.POST['message'], user = user)


    return redirect("/wall")


def post_comment(request):
    user = User.objects.get(id=request.session['id'])
    M = Message.objects.get(id=request.POST['message_id'])

    C = Comment.objects.create(comment=request.POST['comment'],message = M, user = user)

    return redirect("/wall")

def delete(request):
    M = Message.objects.get(id=request.POST['message_id'])

    M.delete()

    return redirect("/wall")
























