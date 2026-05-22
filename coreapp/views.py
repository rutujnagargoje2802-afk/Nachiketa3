from django.shortcuts import render
from .models import GalleryItem # Import your new model
from django.http import HttpResponse




# Ensure this name matches 'views.home_view' in urls.py
def home(request):
    return render(request,'Home.html')


def about(request):
    return render(request,'About.html')




def gallery(request): # Rename this to match your actual gallery view name
    # Filter items by category from the database
    youth_images = GalleryItem.objects.filter(category='youth')
    internship_images = GalleryItem.objects.filter(category='internship')
    community_images = GalleryItem.objects.filter(category='community')
    award_images = GalleryItem.objects.filter(category='award')

    context = {
        'youth_images': youth_images,
        'internship_images': internship_images,
        'community_images': community_images,
        'award_images': award_images,
    }
    return render(request, 'gallery.html', context) # Replace 'gallery.html' with your template name

# Make sure it is imported from coreapp


