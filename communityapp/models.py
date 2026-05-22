from django.db import models
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import models
from django.contrib.auth.models import User# FIXED: Imports the table structure



class Testimonial(models.Model):
    author_name = models.CharField(
        max_length=100,
        help_text="e.g., Student Participant, School Partner"
    )

    quote = models.TextField(
        help_text="The feedback or quote text"
    )

    image = models.ImageField(
        upload_to='testimonials/',
        blank=True,
        null=True,
        help_text="Optional author picture"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} - {self.quote[:30]}..."
    

    
    
    
    
    # clubs/models.py

class JoinClub(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField()

    college = models.CharField(
        max_length=300,
        blank=True
    )

    interest = models.CharField(max_length=200)

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.name
    

    

class Club(models.Model):

    creator_name = models.CharField(max_length=200)

    creator_email = models.EmailField()

    club_name = models.CharField(max_length=300)

    organization = models.CharField(max_length=300)

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.club_name
    

   
# NOTICE: There are absolutely no import lines pointing to .models here!

class YouthProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    project_title = models.CharField(max_length=255)
    category = models.CharField(max_length=150)
    proposal = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project_title

