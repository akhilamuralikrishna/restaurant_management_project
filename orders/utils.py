import secrets
import string
from .models import Order
from datetime import datetime
import django.db.models import Sum

def generate_coupon_code(length=10):
    characters= string.ascii_letters + string.digits

    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if not Order.objects.filter(coupon_code=code).exists():
            return code
def get_daily_sales_total(date=datetime):
    orders=Order.objects.filter(created_at__date=date.date())
    result=orders.aggregate(otal=Sum('total_price'))
    return result['total'] or 0            