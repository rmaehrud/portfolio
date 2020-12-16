from django.contrib import admin
from .models import BlogData,BigData,Link
# Register your models here.
class BigDataAdmin(admin.ModelAdmin):
    list_display = (
        'object_type',
        'text',
        'button_title',
    )
    list_display_links = (
        'object_type',
        'text',
        'button_title',
    )
admin.site.register(BigData,BigDataAdmin)
admin.site.register(BlogData)
admin.site.register(Link)
