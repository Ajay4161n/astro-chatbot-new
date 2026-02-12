# === zodiac.py ===
def get_zodiac_info(dob):
    month = dob.month
    day = dob.day

    zodiac_signs = [
        ("Capricorn", (12, 22), (1, 19)),
        ("Aquarius", (1, 20), (2, 18)),
        ("Pisces", (2, 19), (3, 20)),
        ("Aries", (3, 21), (4, 19)),
        ("Taurus", (4, 20), (5, 20)),
        ("Gemini", (5, 21), (6, 20)),
        ("Cancer", (6, 21), (7, 22)),
        ("Leo", (7, 23), (8, 22)),
        ("Virgo", (8, 23), (9, 22)),
        ("Libra", (9, 23), (10, 22)),
        ("Scorpio", (10, 23), (11, 21)),
        ("Sagittarius", (11, 22), (12, 21)),
    ]

    for sign, start, end in zodiac_signs:
        if (month == start[0] and day >= start[1]) or (month == end[0] and day <= end[1]):
            break

    traits = {
        "Aries": "Energetic, courageous, determined",
        "Taurus": "Reliable, patient, practical",
        "Gemini": "Curious, adaptable, witty",
        "Cancer": "Emotional, nurturing, intuitive",
        "Leo": "Confident, creative, generous",
        "Virgo": "Analytical, loyal, kind",
        "Libra": "Diplomatic, fair, sociable",
        "Scorpio": "Passionate, resourceful, intense",
        "Sagittarius": "Adventurous, optimistic, honest",
        "Capricorn": "Disciplined, responsible, ambitious",
        "Aquarius": "Independent, progressive, inventive",
        "Pisces": "Empathetic, artistic, wise",
    }

    return sign, traits.get(sign, "Unknown traits")

