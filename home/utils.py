from datetime import datetime, time
def is_restaurant_open():
    opening_time = time(8,0)
    closing_time = time(22,0)
    now = datetime.now().time()
    if opening_time <= now <= closing_time:
        return True
    else:
        return False    