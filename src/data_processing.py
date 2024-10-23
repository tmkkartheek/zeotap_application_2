from datetime import datetime
import sqlite3

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def process_weather_data(weather_data):
    try:
        main_data = weather_data['main']
        temp = kelvin_to_celsius(main_data['temp'])
        feels_like = kelvin_to_celsius(main_data['feels_like'])
        weather_condition = weather_data['weather'][0]['main']
        
        return {
            'temperature': temp,
            'feels_like': feels_like,
            'condition': weather_condition,
            'timestamp': datetime.fromtimestamp(weather_data['dt'])
        }
    except KeyError as e:
        print(f"Error processing weather data: {e}")
        return None

def aggregate_weather_data(daily_data):
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

def setup_database():
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

def save_daily_summary(db_file, data_summary):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Assuming data_summary is a dictionary with the required fields
    cursor.execute('''
        INSERT OR REPLACE INTO daily_summary (date, avg_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?)
    ''', (data_summary['date'], data_summary['avg_temp'], data_summary['max_temp'], data_summary['min_temp'], data_summary['dominant_condition']))
    
    conn.commit()
    conn.close()

