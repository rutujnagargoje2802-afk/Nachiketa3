import csv
from django.contrib import admin
from django.http import HttpResponse
from .models import InternshipApplication, YouthClubApplication, ImpactApplication

# 1. Create a reusable function to export data to CSV/Excel
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={opts.verbose_name_plural}.csv'
    writer = csv.writer(response)
    
    # Write the header row automatically using field names
    fields = [field.name for field in opts.fields if not field.many_to_many and not field.one_to_many]
    writer.writerow(fields)
    
    # Write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field)
            data_row.append(value)
        writer.writerow(data_row)
        
    return response

# Add a clean label for the admin dropdown menu
export_to_csv.short_description = "📊 Export Selected to Excel/CSV"


# 2. Register Models with the Export Action Enabled
@admin.register(InternshipApplication)
class InternshipApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'internship_track', 'submitted_at')
    search_fields = ('full_name', 'email')
    list_filter = ('internship_track',)
    actions = [export_to_csv] # <--- Adds the export button

@admin.register(YouthClubApplication)
class YouthClubApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'interest', 'submitted_at')
    search_fields = ('full_name', 'email')
    list_filter = ('interest', 'experience')
    actions = [export_to_csv] # <--- Adds the export button

@admin.register(ImpactApplication)
class ImpactApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'initiative', 'submitted_at')
    search_fields = ('full_name', 'email')
    list_filter = ('initiative',)
    actions = [export_to_csv] # <--- Adds the export button
