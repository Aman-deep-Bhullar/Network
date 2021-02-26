import json
from datetime import timezone

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


from .forms import  ListForm
from .models import User, Item, Follower, Lk

from django.core.paginator import Paginator


def index(request):
    return render(request, "network/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")




def addpost(request):
    if request.method == "POST":
        item = request.POST.get("textarea")
        user = request.user
        item_obj = Item.objects.create(owner=user, post=item)
        item_obj.save()
        return HttpResponseRedirect(reverse("allpost"))









def allpost(request):

           user=request.user

           posts = Item.objects.all()


           ll = Lk.objects.filter(Users=user).count()
           paginator = Paginator(posts, 10)
           if request.GET.get("page") != None:
               try:
                   posts = paginator.page(request.GET.get("page"))
               except:
                   posts = paginator.page(1)
           else:
               posts = paginator.page(1)

           return render(request, "network/Post.html", {'posts': posts, 'll': ll})



def userProfile(request, username):
        if request.method == 'GET':
            currentuser = request.user

            user=User.objects.get(username=username)
            isitfollowing=Follower.objects.filter(follower=currentuser,followed=user).last()
            posts = Item.objects.filter(owner=user).order_by('id').reverse()
            following_count=Follower.objects.filter(follower=user).count()
            follower_count=Follower.objects.filter(followed=user).count()

            paginator = Paginator(posts, 10)
            if request.GET.get("page") != None:
                try:
                    posts = paginator.page(request.GET.get("page"))
                except:
                    posts = paginator.page(1)
            else:
                posts = paginator.page(1)
            return render(request, "network/profile.html",{'user':user,'posts':posts,'following_count':following_count,'follower_count':follower_count,'isitfollowing':isitfollowing})


def following(request,username):
    if request.method == 'GET':
        currentuser = get_object_or_404(User, username=username)
        follows = Follower.objects.filter(follower=currentuser)
        posts = Item.objects.all().order_by('id').reverse()
        posted = []
        for p in posts:
            for follower in follows:
                if follower.followed == p.owner:
                    posted.append(p)
        paginator = Paginator(posts, 10)
        if request.GET.get("page") != None:
            try:
                posts = paginator.page(request.GET.get("page"))
            except:
                posts = paginator.page(1)
        else:
            posts = paginator.page(1)




        return render(request, 'network/Following.html', {'posts':posts})











def follow(request,followed_id):
     followed = User.objects.get(pk=followed_id)
     follower = request.user
     addnewfollow = Follower(follower=follower, followed=followed)
     addnewfollow.save()
     return HttpResponseRedirect(reverse("userprofile", kwargs={'username': followed.username}))

def unfollow(request, unfollowed_id):
     unfollowed = User.objects.get(pk=unfollowed_id)
     unfollower = request.user

     deletenewfollow = Follower.objects.get(follower=unfollower, followed=unfollowed)
     deletenewfollow.delete()

     return HttpResponseRedirect(reverse("userprofile",kwargs={'username':unfollowed.username}))





def edit(request, it_id):
    item = Item.objects.get(pk=it_id)
    form = ListForm(request.POST or None, instance=item)
    if request.method == 'POST':


        if form.is_valid():
            form.save()
            messages.success(request,('Item has been Edited'))
            return redirect('allpost')


    return render(request, 'network/edit.html', {
            'item': item,
            'form': form
        })


def lk(request,item_id):
    post = Item.objects.get(pk=item_id)

    user=request.user
    newlk=Lk(Users=user, post=post)
    newlk.save()

    return HttpResponseRedirect(reverse("allpost"))



def unlike(request, item_id):
    post= Item.objects.get(pk=item_id)
    user = request.user

    deletenewlike = Lk.objects.filter(Users=user, post=post)
    deletenewlike.delete()


    return HttpResponseRedirect(reverse("allpost"))





















