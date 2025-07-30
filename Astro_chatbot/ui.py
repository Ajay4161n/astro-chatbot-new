# ui.py
import tkinter as tk
from astrology_core import get_zodiac_sign, get_planet_positions, get_lagna_sign
from birth_data import get_user_data
from lagna_chart import draw_lagna_chart
from planet_characteristics import interpret_planets

def launch_gui():
    root = tk.Tk()
    root.title("AstroChatbot")
    root.geometry("800x700")

    chat_frame = tk.Text(root, wrap='word', font=("Arial", 12))
    chat_frame.pack(expand=True, fill='both', padx=10, pady=10)

    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    tk.Label(input_frame, text="Name:").grid(row=0, column=0)
    name_entry = tk.Entry(input_frame)
    name_entry.grid(row=0, column=1)

    tk.Label(input_frame, text="Date of Birth (YYYY-MM-DD):").grid(row=1, column=0)
    dob_entry = tk.Entry(input_frame)
    dob_entry.grid(row=1, column=1)

    tk.Label(input_frame, text="Time of Birth (HH:MM):").grid(row=2, column=0)
    tob_entry = tk.Entry(input_frame)
    tob_entry.grid(row=2, column=1)

    tk.Label(input_frame, text="Place of Birth:").grid(row=3, column=0)
    place_entry = tk.Entry(input_frame)
    place_entry.grid(row=3, column=1)

    def respond_to_query():
        name = name_entry.get()
        dob = dob_entry.get()
        tob = tob_entry.get()
        place = place_entry.get()

        chat_frame.delete('1.0', tk.END)  # Clear previous output
        chat_frame.insert(tk.END, f"Hi {name}!\n")
        chat_frame.insert(tk.END, f"Date of Birth: {dob}\n")
        chat_frame.insert(tk.END, f"Time of Birth: {tob}\n")
        chat_frame.insert(tk.END, f"Place of Birth: {place}\n\n")

        zodiac = get_zodiac_sign(dob)
        chat_frame.insert(tk.END, f"Your Zodiac sign is {zodiac['sign']} - {zodiac['traits']}\n\n")

        ascendant = get_lagna_sign(dob, tob, place)
        chat_frame.insert(tk.END, f"Your Ascendant (Lagna) is {ascendant}\n\n")

        planets = get_planet_positions(dob, tob, place)
        chart_text = draw_lagna_chart(ascendant, planets)
        chat_frame.insert(tk.END, f"Lagna Chart:\n{chart_text}\n")

        interpretations = interpret_planets(planets)
        for interp in interpretations:
            chat_frame.insert(tk.END, f"{interp}\n")

    btn = tk.Button(root, text="Generate Astrology Report", command=respond_to_query, font=("Arial", 12), bg="#4CAF50", fg="white")
    btn.pack(pady=10)

    root.mainloop()

       