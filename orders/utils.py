import secrets
import string
from .models import Order

def generate_coupon_code(length=10):
    characters= string.ascii_letters + string.digits

    while True:
        code=''.join(secrets.choice(characters) for _ in range(length))
        if not Order.objects.filter(coupon_code=code).exists():
            return code