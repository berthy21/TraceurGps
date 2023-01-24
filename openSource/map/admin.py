from django.contrib import admin
from .models import User,Member,Addresse

# Register your models here.

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','password','groupe')
    

admin.site.register(Member)

@admin.register(Addresse)

class Address(admin.ModelAdmin):
    list_display = ('address','id')
