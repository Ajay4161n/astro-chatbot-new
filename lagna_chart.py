# === lagna_chart.py ===
from datetime import datetime

ZODIAC_SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

def estimate_lagna(hour, minute):
    """Estimates the Lagna sign based on time of birth (every 2-hour = one sign)."""
    total_minutes = hour * 60 + minute
    index = (total_minutes // 120) % 12
    return ZODIAC_SIGNS[index]

def get_lagna_info(date_str, time_str, place_str):
    """
    Accepts birth date, time, and place.
    Returns estimated Lagna sign and dummy planetary positions.
    """
    try:
        dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
        lagna = estimate_lagna(dt.hour, dt.minute)

        # Dummy planet positions for simplicity (real astrology would need ephemeris)
        dummy_planets = {
            "Sun": "House 1",
            "Moon": "House 2",
            "Mars": "House 3",
            "Mercury": "House 4",
            "Jupiter": "House 5",
            "Venus": "House 6",
            "Saturn": "House 7",
            "Rahu": "House 8",
            "Ketu": "House 9"
        }

        return lagna, dummy_planets

    except Exception as e:
        raise ValueError(f"Invalid input for Lagna calculation: {e}")
