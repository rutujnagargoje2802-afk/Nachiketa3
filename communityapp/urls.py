from django.urls import path
from . import views

urlpatterns = [
  
    path('community/', views.community, name='community'),
    path('youthclub/', views.youthclub, name='youthclub'),
    path('magzine/',views.magzine, name ='magzine'),
    path('youthclub/join/<int:club_id>/', views.join_existing_club, name='join_existing_club'),
    path('submit-project/', views.submit_project_view, name='submit_project'),
]

