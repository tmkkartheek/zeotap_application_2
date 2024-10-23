import matplotlib.pyplot as plt
import sqlite3
from datetime import datetime

def fetch_weather_data(city):
    # Your existing fetch_weather_data implementation
    pass

def process_weather_data(weather_data):
    # Your existing process_weather_data implementation
    pass

def aggregate_weather_data(daily_data):
    # Your existing aggregate_weather_data implementation
    pass

def plot_temperature_trends(db_file):
    """Plot temperature trends from the historical weather data stored in the database."""
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Retrieve historical weather data
    cursor.execute('SELECT date, avg_temp, max_temp, min_temp FROM daily_summary ORDER BY date')
    rows = cursor.fetchall()
    
    conn.close()
    
    # Prepare data for plotting
    dates = []
    avg_temps = []
    max_temps = []
    min_temps = []
    
    for row in rows:
        date = row[0]  # Date
        avg_temp = row[1]  # Average Temperature
        max_temp = row[2]  # Maximum Temperature
        min_temp = row[3]  # Minimum Temperature
        
        # Append data to lists
        dates.append(datetime.strptime(date, '%Y-%m-%d'))  # Convert string to datetime
        avg_temps.append(avg_temp)
        max_temps.append(max_temp)
        min_temps.append(min_temp)

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(dates, avg_temps, label='Average Temperature (°C)', marker='o')
    plt.plot(dates, max_temps, label='Maximum Temperature (°C)', linestyle='--', marker='^')
    plt.plot(dates, min_temps, label='Minimum Temperature (°C)', linestyle='--', marker='v')
    
    # Formatting the plot
    plt.title('Temperature Trends Over Time')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    
    # Show the plot
    plt.tight_layout()
    plt.show()
