from django.contrib import admin
import csv
# Register your models here.
from .models import GalleryItem
from django.http import HttpResponse


# Reusable function to export records to an Excel spreadsheet
def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={opts.verbose_name_plural}.csv'
    writer = csv.writer(response)
    
    # Generate columns based on model database structure fields
    fields = [field.name for field in opts.fields if not field.many_to_many and not field.one_to_many]
    writer.writerow(fields)
    
    # Write entries rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field)
            data_row.append(value)
        writer.writerow(data_row)
        
    return response

export_to_csv.short_description = "📊 Export Selected to Excel/CSV"

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'uploaded_at')
    list_filter = ('category',)
    search_fields = ('title', 'description')
    actions = [export_to_csv]
