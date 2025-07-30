# astrology_core.py

from datetime import datetime

def get_zodiac_sign(dob_str):
    dob = datetime.strptime(dob_str, "%Y-%m-%d")
    month = dob.month
    day = dob.day

    zodiac_signs = [
        ((1, 20), (2, 18), "Aquarius", "innovative and visionary"),
        ((2, 19), (3, 20), "Pisces", "empathic and dreamy"),
        ((3, 21), (4, 19), "Aries", "bold and energetic"),
        ((4, 20), (5, 20), "Taurus", "grounded and reliable"),
        ((5, 21), (6, 20), "Gemini", "curious and expressive"),
        ((6, 21), (7, 22), "Cancer", "sensitive and protective"),
        ((7, 23), (8, 22), "Leo", "charismatic and creative"),
        ((8, 23), (9, 22), "Virgo", "analytical and humble"),
        ((9, 23), (10, 22), "Libra", "balanced and social"),
        ((10, 23), (11, 21), "Scorpio", "intense and mysterious"),
        ((11, 22), (12, 21), "Sagittarius", "optimistic and adventurous"),
        ((12, 22), (1, 19), "Capricorn", "disciplined and wise")
    ]

    for start, end, sign, traits in zodiac_signs:
        start_month, start_day = start
        end_month, end_day = end
        if ((month == start_month and day >= start_day) or
            (month == end_month and day <= end_day)):
            return {"sign": sign, "traits": traits}
    return {"sign": "Capricorn", "traits": "disciplined and wise"}  # default fallback

def get_lagna_sign(dob_str, tob_str, place):
    # Simulate using only hour, more accurate method would require sidereal time
    hour = int(tob_str.split(":")[0])
    minute = int(tob_str.split(":")[1])
    total_minutes = hour * 60 + minute
    index = (total_minutes // 120) % 12  # Each lagna ~2 hours
    lagnas = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    return lagnas[index]

def get_planet_positions(dob_str, tob_str, place):
    # You can replace this with actual data later
    from random import randint
    return {
        "Sun": randint(1, 12),
        "Moon": randint(1, 12),
        "Mars": randint(1, 12),
        "Mercury": randint(1, 12),
        "Jupiter": randint(1, 12),
        "Venus": randint(1, 12),
        "Saturn": randint(1, 12),
        "Rahu": randint(1, 12),
        "Ketu": randint(1, 12)
    }
