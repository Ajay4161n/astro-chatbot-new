# lagna_chart.py
def draw_lagna_chart(ascendant, planets):
    chart = ""
    for i in range(1, 13):
        contents = [k for k, v in planets.items() if v == i]
        content_str = ", ".join(contents)
        chart += f"House {i}: {content_str}\n"
    return chart
