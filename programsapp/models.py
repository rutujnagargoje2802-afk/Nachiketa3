from django.db import models

# CRITICAL: It MUST have (models.Model) inside the parentheses!
class InternshipApplication(models.Model): 
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    college = models.CharField(max_length=200, blank=True, null=True)
    internship_track = models.CharField(max_length=100)
    motivation = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

 
class YouthClubApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    college = models.CharField(max_length=200, blank=True, null=True)
    experience = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)
    motivation = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.interest}"

# Keep your existing InternshipApplication and YouthClubApplication models above...

class ImpactApplication(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    initiative = models.CharField(max_length=150)
    idea = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.initiative}"
