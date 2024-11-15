import requests
import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Replace with your actual OpenWeatherMap API key
API_KEY = "d28057b8ccf2efb88608f67e49612b41"

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        # GUI Elements
        self.city_label = tk.Label(root, text="Enter City:")
        self.city_label.pack()

        self.city_entry = tk.Entry(root)
        self.city_entry.pack()

        self.fetch_button = tk.Button(root, text="Get Weather", command=self.get_weather)
        self.fetch_button.pack()

        self.result_text = tk.Text(root, height=15, width=50)
        self.result_text.pack()

        self.save_button = tk.Button(root, text="Save Data", command=self.save_weather_data)
        self.save_button.pack()

    def get_weather(self):
        """Fetches and displays weather data for the specified city."""
        city = self.city_entry.get()
        if not city:
            messagebox.showerror("Input Error", "Please enter a city name.")
            return

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()
            self.display_weather(weather_data)
        except requests.exceptions.RequestException as e:
            messagebox.showerror("API Error", f"Could not retrieve data: {e}")

    def display_weather(self, weather_data):
        """Parses and displays the fetched weather data."""
        if weather_data.get("cod") != 200:
            messagebox.showerror("City Error", weather_data.get("message", "City not found."))
            return

        city = weather_data["name"]
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        weather_desc = weather_data["weather"][0]["description"].capitalize()
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        self.result_text.delete("1.0", tk.END)
        result = (
            f"Weather in {city}:\n"
            f"Temperature: {temp}°C\n"
            f"Feels like: {feels_like}°C\n"
            f"Description: {weather_desc}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
            f"Time of report: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        self.result_text.insert(tk.END, result)

    def save_weather_data(self):
        """Saves the displayed weather data to a file."""
        data = self.result_text.get("1.0", tk.END).strip()
        if not data:
            messagebox.showerror("Save Error", "No data to save.")
            return

        filename = f"weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, "w") as file:
            file.write(data)
        messagebox.showinfo("Save Success", f"Weather data saved to {filename}")

# Running the Weather App
if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
