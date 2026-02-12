# === birth_details.py ===
from datetime import datetime

def get_birth_details():
    date_input = input("Enter your Date of Birth (YYYY-MM-DD): ")
    time_input = input("Enter your Time of Birth (HH:MM in 24hr format): ")
    place_input = input("Enter your Place of Birth (City, Country): ")

    dob = datetime.strptime(date_input, "%Y-%m-%d")
    tob = datetime.strptime(time_input, "%H:%M").time()

    return dob, tob, place_input
