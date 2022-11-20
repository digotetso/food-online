# ••• CREATE / UPDATE the UserProfile right after the user is created / modified 

from .models import User, UserProfile
from django.db.models.signals import  post_save, pre_save
from django.dispatch import receiver


# A function below connects reciver to a signal? and sender(User) (#1 and #2)
# Now "post_save_create_profile_reciever" each time after User is save in db
#1 receiver ---> post_save_create_profile_reciever
#2 signal ---> post_save
#3 sender ----> User(model)

@receiver(post_save, sender=User)
def post_save_create_profile_reciever(sender, instance, created, **kwargs): # created flag
    print(created)
    if created:
        # if the 'User' is created(will be True), create user profile
        UserProfile.objects.create(user=instance)
        print('user profile is created')
    else: 
        # When the user is updated, 
        try:
            # Save the existing profile with uppdated "user" information
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # If there this user instance (user=instance) does not have a profile, 
            # then create the profile
            UserProfile.objects.create(user=instance)
            print('profile didnt exist, but one has been created')
        print('User updated')
            

@receiver(pre_save, sender=User)
def pre_save_profile_recivver(sender, instance, **kwargs): # doesnt take created flag
    print(instance.username, 'this user is being saved')


