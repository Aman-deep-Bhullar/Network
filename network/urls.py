
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("addpost", views.addpost, name="addpost"),
    path("all",views.allpost, name="allpost"),
    path("lk/<int:item_id>", views.lk, name="lk"),
    path("unlike/<int:item_id>", views.unlike, name="unlike"),
    path("edit/<int:it_id>", views.edit, name="edit"),
    path("profile/<str:username>", views.userProfile, name="userprofile"),
    path('follow/<int:followed_id>', views.follow, name="follow"),
    path('unfollow/<int:unfollowed_id>', views.unfollow, name="unfollow"),
    path("following/<str:username>", views.following, name="following"),



   ]

