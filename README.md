# Weather Monitoring System

## Overview
The Weather Monitoring System is a Python-based application that retrieves real-time weather data for major cities in India from the OpenWeatherMap API. It aggregates daily weather statistics, including average, maximum, and minimum temperatures, and stores this data in an SQLite database. The system can also visualize temperature trends over time.

## Features
- Fetches real-time weather data for multiple cities.
- Aggregates daily weather statistics: average, maximum, and minimum temperatures.
- Stores weather data in an SQLite database.
- Generates temperature trends visualizations using Matplotlib.

## Requirements
- Python 3.x
- Required libraries:
  - `requests`
  - `sqlite3` (built-in)
  - `matplotlib`
  - `logging`
  
## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd weather-monitoring-system
   ```

2. Install the required libraries:
   ```bash
   pip install requests matplotlib
   ```

3. Get your API key from OpenWeatherMap by signing up at [OpenWeatherMap](https://openweathermap.org/).

4. Replace the placeholder in the code with your actual API key:
   ```python
   API_KEY = 'your_api_key_here'
   ```

## Usage
Run the application with the following command:
```bash
python src/main.py
```

The program will continuously fetch weather data every 5 minutes. It logs errors to `weather_monitoring.log` and saves daily summaries to `weather_data.db`.

## Viewing Historical Data
You can view the stored historical weather data by querying the SQLite database or by implementing additional functions to display data.

## Plotting Temperature Trends
The system generates a plot of temperature trends based on historical data. This functionality can be called after collecting data in the database.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [OpenWeatherMap](https://openweathermap.org/) for the weather data API.
- [Matplotlib](https://matplotlib.org/) for data visualization.
```

### Customization:
- Replace `<repository-url>` with the actual URL of your GitHub repository.
- Adjust any sections or details based on your project's specific needs or any additional features you might want to include.
