from django.contrib import admin
from .models import Profile, Post



# class imageAdmin(admin.ModelAdmin):
#     list_display = ["title","image", "likes","dislikes"]

admin.site.register(Post)
admin.site.register(Profile)
