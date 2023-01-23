from django.contrib import admin
from .models import User,Member

# Register your models here.

@admin.register(User)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','password','groupe')
    

admin.site.register(Member)