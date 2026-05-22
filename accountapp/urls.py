from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),  # <-- Make sure name='signup' is here!
     path('logout/', views.logout_view, name='logout'), 
]