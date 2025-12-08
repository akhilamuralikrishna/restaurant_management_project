from django.contrib import admin
from .models import Order 

# Register your models here.
def mark_as_processed(modeladmin, request, queryset):
    queryset.update(status='processed')
mark_as_processed.short_description = 'Mark Selected orders as a Processed'

class OrderAdmin(admin.Modeladmin):
    list_display = ('id','user','status','created_at')
    actions = [mark_as_processed]
admin.site.register(Order, OrderAdmin)    
