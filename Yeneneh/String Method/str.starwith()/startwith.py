text = "sky is yellow"

# Checking
starts_with_today = text.startswith("sky")      # Should return True
starts_with_laundry = text.startswith("yellow")   # Should return False
starts_with_today_lower = text.startswith("sky")  # Should return False (case-sensitive)

# To Print
print(f"Starts with 'sky': {starts_with_today}")          # Output: True
print(f"Starts with 'yellow': {starts_with_laundry}")      # Output: False
print(f"Starts with 'sky': {starts_with_today_lower}")    # Output: False
