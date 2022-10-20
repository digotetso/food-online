from django.db import models

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,first_name, last_name, username, email, password=None):

        if not email:
            raise ValueError('User must have email address')
        
        if not username:
            raise ValueError('User must have username address')


        user = self.model(
            email = self.normalize_email(email),
            username =  username,
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password)
        user.save(using=self._db) # save on our default db

        return user

    def create_superuser(self,first_name, last_name, username, email, password=None):
       
        user = self.model(
            email = self.normalize_email(email),
            username =  username,
            password=password,
            first_name = first_name,
            last_name = last_name,

        )

        # For my model to be compatible with admin, i have to implement the following
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.is_admin = True

        # it will hash the password
        user.set_password(password)
        user.save(using=self._db)
        return user
        

class User(AbstractBaseUser):
    VENDOR = 1
    CUSTOMER = 2

    ROLE_CHOICE = (
        (VENDOR, 'Vendor'),
        (CUSTOMER, 'Customer'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)


     #For my model to be compatible with admin, atlest implement: is_staff, is_active,_has_perm(),has_module_perm()

    # required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # will be used as a username    
    USERNAME_FIELD = 'email'
    # will be prompted / required when creating a user --> ie python3 manage.py createsuperuser
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

