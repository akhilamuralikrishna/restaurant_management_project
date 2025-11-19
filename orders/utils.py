import secrets
import string
from .models import Order
from datetime import datetime
from django.db.models import Sum
from decimal import Decimal

def generate_coupon_code(length=10):
    characters= string.ascii_letters + string.digits

    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if not Order.objects.filter(coupon_code=code).exists():
            return code
def get_daily_sales_total(date=datetime):
    orders=Order.objects.filter(created_at__date=date.date())
    result=orders.aggregate(total=Sum('total_price'))
    return result['total'] or 0
def calculate_tip_amount(order_total,tip_percentage):
    order_total=Decimal(order_total)
    tip_amount=order_total*Decimal(tip_percentage)/Decimal(100)
    return round(tip_amount,2)    
