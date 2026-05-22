from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import Testimonial, JoinClub, Club
from .models import YouthProject
# 1. COMMUNITY VIEW
def community(request):
    testimonials = Testimonial.objects.all().order_by('-created_at')
    context = {
        'testimonials': testimonials,
    }
    return render(request, 'community.html', context)


# 2. YOUTHCLUB VIEW (Deduplicated & Merged Logic)
def youthclub(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        # JOIN CLUB FORM
        if form_type == "join_club":
            JoinClub.objects.create(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                college=request.POST.get("college"),
                interest=request.POST.get("interest")
            )
            messages.success(request, "Successfully joined the club!")
            return redirect('youthclub')

        # CREATE CLUB FORM
        elif form_type == "create_club":
            Club.objects.create(
                creator_name=request.POST.get("creator_name"),
                creator_email=request.POST.get("creator_email"),
                club_name=request.POST.get("club_name"),
                organization=request.POST.get("organization"),
                description=request.POST.get("description")
            )
            messages.success(request, "Your new club has been created successfully!")
            return redirect('youthclub')

    # GET Request logic
    clubs = Club.objects.all()
    context = {
        'clubs': clubs
    }
    return render(request, 'youthclub.html', context)


# 3. JOIN EXISTING CLUB VIEW (FIXED TYPO HERE)
def join_existing_club(request, club_id):
    # FIXED: Changed 400 to 404
    club = get_object_or_404(Club, id=club_id)
    
    messages.success(request, f"Successfully requested to join {club.club_name}!")
    return redirect('youthclub')

# This is correct here in views.py

def submit_project_view(request):
    if request.method == "POST":
        project_title = request.POST.get('project_title')
        category = request.POST.get('category')
        proposal = request.POST.get('proposal')
        
        word_count = len(proposal.split())
        if word_count > 500:
            messages.error(request, f"Your proposal is too long ({word_count} words). Please reduce it under 500 words.")
            return render(request, 'submit_project.html')
            
        YouthProject.objects.create(
            user=request.user if request.user.is_authenticated else None,
            project_title=project_title,
            category=category,
            proposal=proposal
        )
        
        messages.success(request, f"Project '{project_title}' has been submitted successfully for review!")
        return redirect('community')
        
    return render(request, 'submit_project.html')




# 4. MAGAZINE VIEW
def magzine(request):
    return render(request, 'magzine.html')
