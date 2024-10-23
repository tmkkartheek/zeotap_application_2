# Weather Monitoring System

Overview 
The Weather Monitoring System is a Python application that retrieves and processes real
time weather data for major metropolitan cities in India using the OpenWeatherMap API. The 
application stores daily weather summaries in a SQLite database and provides visualizations 
of temperature trends. 


Features 
1. Real-time Weather Data Retrieval: - Fetches current weather data for specified cities, including temperature and weather 
conditions. 
2. SQLite Database Integration: - Stores daily weather summaries in a SQLite database. - Historical data includes average temperature, maximum temperature, minimum 
temperature, and     
dominant weather condition. 
3. Data Aggregation: - Aggregates weather data from multiple cities to provide overall daily summaries. 
4. Data Visualization: - Plots temperature trends using Matplotlib based on historical weather data stored in the 
database. 
5. Error Logging: - Logs errors encountered during API calls for better troubleshooting.


Installation 
To run the application, ensure you have Python installed and follow these steps: 
1. Clone the repository: 
```bash 
git clone https://github.com/tmkkartheek/zeotap_application_2.git 
cd weather-monitoring-system 
``` 
2. Install the required libraries: 
```bash 
pip install requests matplotlib 
``` 
3. Obtain an API key from OpenWeatherMap and replace it in the code. 
4. Run the application: 
```bash 
python src/main.py 
```


Usage 
- The application fetches weather data every 5 minutes. 
- Console output displays real-time weather information and aggregated data summaries.
- - Historical weather data can be visualized through temperature trend plots. 


Technologies Used -Programming Language: Python -Database: SQLite -Other Libraries: 
 requests for API calls 
 logging for error handling and logging 
 datetime for date handling 
 matplotlib for plotting temperature trends 

![image](https://github.com/user-attachments/assets/e15d420d-565f-42ae-b30c-1df64961ef27)


Acknowledgments - OpenWeatherMap for providing weather data. - Matplotlib for data visualization. - SQLite for lightweight database management.

![image](https://github.com/user-attachments/assets/227e2941-e40f-4428-9a84-e1a31a772e93)
