from django.urls import path
from .views import signupUser

urlpatterns = [
    path('signup', signupUser, name='signup'),
]