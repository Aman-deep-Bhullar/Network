from django.contrib import admin

# Register your models here.
from network.models import User, Item, Follower

admin.site.register(User)
admin.site.register(Item)


admin.site.register(Follower)



