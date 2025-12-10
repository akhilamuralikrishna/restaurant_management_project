from django.contrib import admin
from .models import Order,OrderStatus

# Register your models here.
@admin.action(description='Mark selected orders as processed')
def mark_as_processed(modeladmin, request, queryset):
    completed_status,created = OrderStatus.objects.get_or_create(name='COMPLETED')
    queryset.updated(status=completed_status)

@admin.register(Order)
class OrderAdmin(admin.Modeladmin):
    list_display = ('id','user','status','created_at')
    actions = [mark_as_completed]
