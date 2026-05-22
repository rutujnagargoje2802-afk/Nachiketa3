from django.apps import AppConfig

# 1. Double M in the class name
class ProgramsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    
    # 2. Make sure this has TWO 'm's!
    name = 'programsapp'  

