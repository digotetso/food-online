from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile

# Register your models here.
# To subclass 'UserAdmin', for custom user extending ABU, you’ll need to override any of the definitions that refer to fields on 
# django.contrib.auth.models.AbstractUser that aren’t on your custom user class.
# e.g filter_horizontal is uses 'groups' field [see django UserAdmin] which I didnt define in my custom model, so I need to overide this field
class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'first_name','last_name','role','is_active', 'username')
    list_filter =('email',)
    ordering = ('-date_joined',)  
    fieldsets = ()
    filter_horizontal =()

admin.site.register(User,UserAdmin)
admin.site.register(UserProfile)

