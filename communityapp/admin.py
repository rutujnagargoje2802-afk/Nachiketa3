from django.contrib import admin
import csv
from django.http import HttpResponse

from .models import Testimonial
from .models import JoinClub
from .models import Club


from .models import  YouthProject

# Reusable function to export records to CSV
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = (
        f'attachment; filename={opts.verbose_name_plural}.csv'
    )

    writer = csv.writer(response)

    # Generate columns automatically
    fields = [
        field.name
        for field in opts.fields
        if not field.many_to_many and not field.one_to_many
    ]

    writer.writerow(fields)

    # Write data rows
    for obj in queryset:
        data_row = []

        for field in fields:
            value = getattr(obj, field)
            data_row.append(value)

        writer.writerow(data_row)

    return response


export_to_csv.short_description = "📊 Export Selected to Excel/CSV"


# Register Testimonials model
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'created_at')
    search_fields = ('author_name', 'quote')
    actions = [export_to_csv]






# ===================================
# EXPORT TO CSV FUNCTION
# ===================================

def export_to_csv(modeladmin, request, queryset):

    opts = modeladmin.model._meta

    response = HttpResponse(
        content_type='text/csv'
    )

    response['Content-Disposition'] = (

        f'attachment; filename='
        f'{opts.verbose_name_plural}.csv'

    )

    writer = csv.writer(response)

    # AUTO GENERATE FIELDS

    fields = [

        field.name

        for field in opts.fields

        if not field.many_to_many
        and not field.one_to_many

    ]

    writer.writerow(fields)

    # DATA ROWS

    for obj in queryset:

        row = []

        for field in fields:

            value = getattr(obj, field)

            row.append(value)

        writer.writerow(row)

    return response


export_to_csv.short_description = (

    "📊 Export Selected to Excel/CSV"

)


# ===================================
# CLUB ADMIN
# ===================================

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):

    list_display = (

        'club_name',

        'creator_name',

        'organization',

        'created_at'

    )

    search_fields = (

        'club_name',

        'creator_name',

        'organization'

    )

    list_filter = (

        'created_at',

    )

    actions = [export_to_csv]


# ===================================
# JOIN CLUB ADMIN
# ===================================

@admin.register(JoinClub)
class JoinClubAdmin(admin.ModelAdmin):

    list_display = (

        'name',

        'email',

        'interest',

        'joined_at'

    )

    search_fields = (

        'name',

        'email',

        'interest'

    )

    list_filter = (

        'interest',

        'joined_at'

    )

    actions = [export_to_csv]



# Custom administrative layout interface for Youth Project submissions
class YouthProjectAdmin(admin.ModelAdmin):
    # Columns displayed directly in your dashboard row view grid layout
    list_display = ('project_title', 'category', 'user', 'submitted_at')
    
    # Adds an interactive sidebar search filtering panel tool based on dates
    list_filter = ('category', 'submitted_at')
    
    # Enables global search across titles, categories, and descriptions
    search_fields = ('project_title', 'category', 'proposal')

# Register all your existing models so everything displays in one place

admin.site.register(YouthProject) # Links table with custom visual column dashboard layout
