# === main.py ===
import tkinter as tk
from tkinter import messagebox
from zodiac import get_zodiac_info
from birth_details import get_birth_details
from lagna_chart import get_lagna_info
from planetary_analysis import analyze_planets

def run_astrochatbot():
    try:
        date_input = date_entry.get()
        time_input = time_entry.get()
        place_input = place_entry.get()

        dob, tob, pob = get_birth_details(date_input, time_input, place_input)

        zodiac_sign, zodiac_traits = get_zodiac_info(dob)
        lagna, planet_positions = get_lagna_info(dob, tob, pob)
        analysis = analyze_planets(planet_positions)

        result = f"Your Zodiac Sign is: {zodiac_sign}\n"
        result += f"Personality Traits: {zodiac_traits}\n\n"
        result += f"Your Ascendant (Lagna) is: {lagna}\n\n"
        result += "Planetary Analysis:\n" + "\n".join(analysis)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# --- GUI Setup ---
window = tk.Tk()
window.title("Advanced AstroChatbot 🌌")
window.geometry("600x600")

frame = tk.Frame(window)
frame.pack(pady=20)

tk.Label(frame, text="Date of Birth (YYYY-MM-DD):").grid(row=0, column=0, sticky="w")
date_entry = tk.Entry(frame, width=30)
date_entry.grid(row=0, column=1)

tk.Label(frame, text="Time of Birth (HH:MM 24hr):").grid(row=1, column=0, sticky="w")
time_entry = tk.Entry(frame, width=30)
time_entry.grid(row=1, column=1)

tk.Label(frame, text="Place of Birth (City, Country):").grid(row=2, column=0, sticky="w")
place_entry = tk.Entry(frame, width=30)
place_entry.grid(row=2, column=1)

tk.Button(window, text="Get Astrology Report", command=run_astrochatbot).pack(pady=10)

output_box = tk.Text(window, height=20, width=70)
output_box.pack(pady=10)

window.mainloop()
