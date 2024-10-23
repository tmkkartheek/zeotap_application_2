# src/visualizations.py
import matplotlib.pyplot as plt

def plot_temperature_trends(city, temperatures, dates):
    plt.plot(dates, temperatures, label=f'{city} Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (Celsius)')
    plt.title(f'Temperature Trends for {city}')
    plt.legend()
    plt.show()
