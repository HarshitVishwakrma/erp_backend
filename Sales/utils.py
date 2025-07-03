from datetime import datetime
from .models import onwardchallan

def create_challanNumber():
        current_year = datetime.now().year % 100  # e.g., 25
        next_year = (datetime.now().year + 1) % 100  # e.g., 26
        prefix = f"{current_year:02d}{next_year:02d}"  # '2526'
        
        # Start from 0001 to 9999 (max 4-digit counter)
        for counter in range(1, 10000):
            challan_no = f"{prefix}{counter:05d}"  # '252600001' ... '252609999'
            
            # Ensure uniqueness in DB
            if not onwardchallan.objects.filter(challan_no=challan_no).exists():
                return challan_no

        raise ValueError("No available challan numbers left for the current year range.")
