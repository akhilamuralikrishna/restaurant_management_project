from datetime import datetime, time
def is_restaurant_open():
    opening_time = time(8,0)
    closing_time = time(22,0)
    now = datetime.now().time()
    if opening_time <= now <= closing_time:
        return True
    else:
        return False
import re        
def validate_phone_number(phone):
    '''
    validate a phone number format.
    Accepts:
    - Optional +country code
    - 10 to 12th digits
    - Optional hyphens or spaces
    '''
    pattern = r'^(\+?\d{1,3}[- ]?)?\d{10,12}$'             