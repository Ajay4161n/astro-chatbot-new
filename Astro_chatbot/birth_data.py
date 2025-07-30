# birth_data.py
def get_user_data():
    name = input("Enter your name: ")
    dob = input("Enter DOB (YYYY-MM-DD): ")
    tob = input("Enter Time of Birth (HH:MM): ")
    place = input("Enter Place of Birth: ")
    return name, dob, tob, place
