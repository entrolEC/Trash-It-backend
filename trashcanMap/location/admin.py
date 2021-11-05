from django.contrib import admin
from django.contrib.auth.models import User
from accounts.models import CustomUser
from location.models import Trashcan, Likes, DisLikes

class LikesInline(admin.StackedInline):
    model = Likes
    extra = 0

class DisLikesInline(admin.StackedInline):
    model = DisLikes
    extra = 0
class TrashcanAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'latitude', 'longitude']
    inlines = [LikesInline, DisLikesInline]

admin.site.register(Trashcan, TrashcanAdmin)
admin.site.register(CustomUser)