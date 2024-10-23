# src/alerting.py
def check_threshold(weather_data, threshold):
    if weather_data['temp'] > threshold:
        return True
    return False

def trigger_alert(city, temp):
    print(f"ALERT! Temperature in {city} has crossed the threshold: {temp}C")
