from . import views
from django.urls import path

urlpatterns = [
    path('register-user/', views.register_user, name='register-user')
]
