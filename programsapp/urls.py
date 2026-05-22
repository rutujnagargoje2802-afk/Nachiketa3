from django.urls import path
from . import views

urlpatterns = [
    # Path for your informational page (e.g., http://127.0.0)
    path('', views.programme, name='programme'), 
    
    # Path for your form page (e.g., http://127.0.0apply/)
    path('apply/', views.apply, name='apply'), 
    
    path('speintern/', views.speintern, name='speintern'),
    path('impact/', views.impact, name='impact'),
]
