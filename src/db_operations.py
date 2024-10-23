import sqlite3

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

def save_daily_summary(db_file, summary_data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    date = summary_data['date']
    avg_temp = summary_data['avg_temp']
    max_temp = summary_data['max_temp']
    min_temp = summary_data['min_temp']
    dominant_condition = summary_data['dominant_condition']

    try:
        cursor.execute('''
            INSERT INTO daily_summary (date, avg_temp, max_temp, min_temp, dominant_condition)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(date) DO UPDATE SET
                avg_temp = excluded.avg_temp,
                max_temp = excluded.max_temp,
                min_temp = excluded.min_temp,
                dominant_condition = excluded.dominant_condition;
        ''', (date, avg_temp, max_temp, min_temp, dominant_condition))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error saving to database: {e}")
    finally:
        conn.close()

def retrieve_weather_data(db_file, date=None):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    query = 'SELECT * FROM daily_summary'
    if date:
        query += ' WHERE date = ?'
        cursor.execute(query, (date,))
    else:
        cursor.execute(query)
    
    rows = cursor.fetchall()
    conn.close()
    
    for row in rows:
        print(f"Date: {row[0]}, Avg Temp: {row[1]}, Max Temp: {row[2]}, Min Temp: {row[3]}, Dominant Condition: {row[4]}")
