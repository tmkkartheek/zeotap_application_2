import requests
import sqlite3
import logging
import time
from datetime import datetime
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(filename='weather_monitoring.log', level=logging.ERROR)

# Constants
API_KEY = '20df458f187d1d62ab2bc347e95286dc'  # Replace with your actual API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
UPDATE_INTERVAL = 300  # Update every 5 minutes (300 seconds)

def setup_database():
    """Set up the SQLite database and create a table for daily weather summaries."""
    conn = sqlite3.connect('weather_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_summary (
            date TEXT PRIMARY KEY,
            avg_temp REAL,
            max_temp REAL,
            min_temp REAL,
            dominant_condition TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_weather_data(city):
    """Fetch weather data from OpenWeather API for a specified city."""
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
        return response.json()  # Return the JSON response as a Python dictionary
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching weather data for {city}: {e}")
        logging.error(f"Error fetching weather data for {city}: {e}")
        return {}  # Return an empty dictionary on error

def kelvin_to_celsius(temp_kelvin):
    """Convert temperature from Kelvin to Celsius."""
    return temp_kelvin - 273.15

def process_weather_data(weather_data):
    """Process the raw weather data to extract relevant information."""
    if 'main' in weather_data:
        temp_celsius = kelvin_to_celsius(weather_data['main']['temp'])
        return {
            'temperature': temp_celsius,
            'condition': weather_data['weather'][0]['description']
        }
    return None

def save_daily_summary(db_file, data):
    """Save the daily weather summary to the SQLite database."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    date = datetime.now().strftime('%Y-%m-%d')  # Use current date
    cursor.execute('''
        INSERT OR REPLACE INTO daily_summary (date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, data['avg_temp'], data['max_temp'], data['min_temp'], data['dominant_condition']))
    
    conn.commit()
    conn.close()

def aggregate_weather_data(daily_data):
    """Aggregate daily weather data to calculate average, maximum, and minimum temperatures."""
    if not daily_data:
        return None

    total_temp = 0
    max_temp = float('-inf')
    min_temp = float('inf')
    condition_counts = {}

    for data in daily_data:
        temp = data['temperature']
        total_temp += temp
        max_temp = max(max_temp, temp)
        min_temp = min(min_temp, temp)
        condition = data['condition']
        
        if condition not in condition_counts:
            condition_counts[condition] = 0
        condition_counts[condition] += 1

    avg_temp = total_temp / len(daily_data)
    dominant_condition = max(condition_counts, key=condition_counts.get)

    return {
        'avg_temp': avg_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': dominant_condition,
    }

def retrieve_weather_data(db_file):
    """Retrieve historical weather data from the SQLite database."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM daily_summary')
    
    rows = cursor.fetchall()
    for row in rows:
        print(f"Date: {row[0]}, Avg Temp: {row[1]}, Max Temp: {row[2]}, Min Temp: {row[3]}, Condition: {row[4]}")
    
    conn.close()

def plot_temperature_trends(db_file):
    """Plot temperature trends based on historical data."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT date, avg_temp, max_temp, min_temp FROM daily_summary')
    rows = cursor.fetchall()
    
    dates = [row[0] for row in rows]
    avg_temps = [row[1] for row in rows]
    max_temps = [row[2] for row in rows]
    min_temps = [row[3] for row in rows]
    
    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label='Average Temperature', marker='o')
    plt.plot(dates, max_temps, label='Maximum Temperature', marker='o')
    plt.plot(dates, min_temps, label='Minimum Temperature', marker='o')
    plt.title('Temperature Trends')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
    plt.show()
    conn.close()

def main():
    """Main function to run the weather monitoring system."""
    setup_database()

    while True:
        all_processed_data = []

        for city in CITIES:
            weather_data = fetch_weather_data(city)
            if weather_data:
                processed_data = process_weather_data(weather_data)
                if processed_data:
                    print(f"Processed data for {city}: {processed_data}")
                    all_processed_data.append(processed_data)  # Collect processed data

        # Aggregate daily data
        aggregated_data = aggregate_weather_data(all_processed_data)

        # Save aggregated summary to the database
        if aggregated_data:
            save_daily_summary('weather_data.db', aggregated_data)
            print("Aggregated Weather Data Saved:")
            print(f"Average Temperature: {aggregated_data['avg_temp']} °C")
            print(f"Maximum Temperature: {aggregated_data['max_temp']} °C")
            print(f"Minimum Temperature: {aggregated_data['min_temp']} °C")
            print(f"Dominant Condition: {aggregated_data['dominant_condition']}")

        # Retrieve and display historical data
        print("\nHistorical Weather Data:")
        retrieve_weather_data('weather_data.db')

        # Plotting temperature trends
        plot_temperature_trends('weather_data.db')

        # Wait for the next update
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
