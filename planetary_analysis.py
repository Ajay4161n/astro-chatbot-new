# === planetary_analysis.py ===
def analyze_planets(planet_positions):
    results = []
    for planet, house in planet_positions.items():
        results.append(f"{planet} is in {house}, influencing related life areas.")
    return results
