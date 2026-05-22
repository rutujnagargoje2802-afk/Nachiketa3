from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InternshipApplication, YouthClubApplication, ImpactApplication 

# 1. View to render the informational template page
def programme(request):
    return render(request, 'programme.html')

# 2. Separate View to process and render the application form page
def apply(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        internship_track = request.POST.get('internship_track')
        motivation = request.POST.get('motivation')

        InternshipApplication.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            college=college,
            internship_track=internship_track,
            motivation=motivation
        )

        messages.success(request, 'Your internship application has been received!')
        return redirect('apply')

    # Points cleanly to your new dedicated form page layout
    return render(request, 'apply.html') 



# 3. MOVED: Special Internship Programme database handling goes here!
def speintern(request):
    if request.method == 'POST':
        # Grab values from the HTML inputs
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        college = request.POST.get('college')
        experience = request.POST.get('experience')
        interest = request.POST.get('interest')
        motivation = request.POST.get('motivation')

        # Save record row directly into your PostgreSQL database
        YouthClubApplication.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            college=college,
            experience=experience,
            interest=interest,
            motivation=motivation
        )

        messages.success(request, 'Your Special Internship application has been received successfully!')
        return redirect('speintern') # Redirects back to refresh the form cleanly

    return render(request, 'speintern.html') # Loads your speintern form template page


# Keep your other views (programme, apply, speintern) unchanged...

def impact(request):
    if request.method == 'POST':
        # Retrieve form data using HTML field name attributes
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        initiative = request.POST.get('initiative')
        idea = request.POST.get('idea')

        # Create record row directly inside PostgreSQL
        ImpactApplication.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            initiative=initiative,
            idea=idea
        )

        messages.success(request, 'Your Initiative Application has been submitted successfully!')
        return redirect('impact') # Redirect back to refresh the form cleanly

    return render(request, 'impact.html')
