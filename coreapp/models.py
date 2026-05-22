from django.db import models


class GalleryItem(models.Model):

    CATEGORY_CHOICES = [
        ('youth', 'Youth Programs'),
        ('internship', 'Internship Activities'),
        ('community', 'Community Projects'),
        ('award', 'Student Awards'),
    ]

    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"