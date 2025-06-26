from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Combined Global + Indian Cities Weather Dataset
SAMPLE_WEATHER_DATA = {
    "London": {
        'city': "London",
        'country': "UK",
        'temperature': 22,
        'temp_min': 18,
        'temp_max': 25,
        'description': "Clear Sky",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 55,
        'wind_speed': 4.5,
        'sunrise': datetime.fromtimestamp(1719390000).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719440400).strftime('%I:%M %p')
    },
    "New York": {
        'city': "New York",
        'country': "US",
        'temperature': 27,
        'temp_min': 23,
        'temp_max': 29,
        'description': "Partly Cloudy",
        'icon': "http://openweathermap.org/img/wn/02d@2x.png",
        'humidity': 60,
        'wind_speed': 6.0,
        'sunrise': datetime.fromtimestamp(1719393600).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719444600).strftime('%I:%M %p')
    },
    "Mumbai": {
        'city': "Mumbai",
        'country': "India",
        'temperature': 32,
        'temp_min': 29,
        'temp_max': 35,
        'description': "Humid and Cloudy",
        'icon': "http://openweathermap.org/img/wn/03d@2x.png",
        'humidity': 70,
        'wind_speed': 5.2,
        'sunrise': datetime.fromtimestamp(1719382800).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719433200).strftime('%I:%M %p')
    },
    "Sydney": {
        'city': "Sydney",
        'country': "Australia",
        'temperature': 18,
        'temp_min': 15,
        'temp_max': 20,
        'description': "Rain Showers",
        'icon': "http://openweathermap.org/img/wn/09d@2x.png",
        'humidity': 80,
        'wind_speed': 7.0,
        'sunrise': datetime.fromtimestamp(1719386400).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719436800).strftime('%I:%M %p')
    },
    "Tokyo": {
        'city': "Tokyo",
        'country': "Japan",
        'temperature': 25,
        'temp_min': 22,
        'temp_max': 28,
        'description': "Sunny",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 50,
        'wind_speed': 3.5,
        'sunrise': datetime.fromtimestamp(1719384600).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719435000).strftime('%I:%M %p')
    },
    "Paris": {
        'city': "Paris",
        'country': "France",
        'temperature': 20,
        'temp_min': 17,
        'temp_max': 23,
        'description': "Overcast",
        'icon': "http://openweathermap.org/img/wn/04d@2x.png",
        'humidity': 65,
        'wind_speed': 4.0,
        'sunrise': datetime.fromtimestamp(1719385800).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719436200).strftime('%I:%M %p')
    },
    "Dubai": {
        'city': "Dubai",
        'country': "UAE",
        'temperature': 39,
        'temp_min': 35,
        'temp_max': 42,
        'description': "Hot and Sunny",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 20,
        'wind_speed': 3.0,
        'sunrise': datetime.fromtimestamp(1719382200).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719432600).strftime('%I:%M %p')
    },
    "Singapore": {
        'city': "Singapore",
        'country': "Singapore",
        'temperature': 31,
        'temp_min': 28,
        'temp_max': 33,
        'description': "Thunderstorms",
        'icon': "http://openweathermap.org/img/wn/11d@2x.png",
        'humidity': 75,
        'wind_speed': 5.5,
        'sunrise': datetime.fromtimestamp(1719385200).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719435600).strftime('%I:%M %p')
    },
    "Toronto": {
        'city': "Toronto",
        'country': "Canada",
        'temperature': 19,
        'temp_min': 16,
        'temp_max': 21,
        'description': "Light Rain",
        'icon': "http://openweathermap.org/img/wn/10d@2x.png",
        'humidity': 68,
        'wind_speed': 4.7,
        'sunrise': datetime.fromtimestamp(1719393000).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719443400).strftime('%I:%M %p')
    },
    "Cape Town": {
        'city': "Cape Town",
        'country': "South Africa",
        'temperature': 16,
        'temp_min': 14,
        'temp_max': 18,
        'description': "Windy",
        'icon': "http://openweathermap.org/img/wn/50d@2x.png",
        'humidity': 60,
        'wind_speed': 8.0,
        'sunrise': datetime.fromtimestamp(1719388800).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719439200).strftime('%I:%M %p')
    },
    "Berlin": {
        'city': "Berlin",
        'country': "Germany",
        'temperature': 21,
        'temp_min': 17,
        'temp_max': 24,
        'description': "Cloudy",
        'icon': "http://openweathermap.org/img/wn/04d@2x.png",
        'humidity': 58,
        'wind_speed': 4.0,
        'sunrise': datetime.fromtimestamp(1719387000).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719437400).strftime('%I:%M %p')
    },
    "Madrid": {
        'city': "Madrid",
        'country': "Spain",
        'temperature': 29,
        'temp_min': 25,
        'temp_max': 32,
        'description': "Sunny",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 40,
        'wind_speed': 5.0,
        'sunrise': datetime.fromtimestamp(1719385200).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719435600).strftime('%I:%M %p')
    },
    "Rome": {
        'city': "Rome",
        'country': "Italy",
        'temperature': 27,
        'temp_min': 23,
        'temp_max': 30,
        'description': "Partly Cloudy",
        'icon': "http://openweathermap.org/img/wn/02d@2x.png",
        'humidity': 50,
        'wind_speed': 4.3,
        'sunrise': datetime.fromtimestamp(1719385800).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719436200).strftime('%I:%M %p')
    },
    "Moscow": {
        'city': "Moscow",
        'country': "Russia",
        'temperature': 16,
        'temp_min': 13,
        'temp_max': 18,
        'description': "Rainy",
        'icon': "http://openweathermap.org/img/wn/10d@2x.png",
        'humidity': 75,
        'wind_speed': 5.8,
        'sunrise': datetime.fromtimestamp(1719384000).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719434400).strftime('%I:%M %p')
    },
    "Bangkok": {
        'city': "Bangkok",
        'country': "Thailand",
        'temperature': 33,
        'temp_min': 30,
        'temp_max': 36,
        'description': "Humid with Showers",
        'icon': "http://openweathermap.org/img/wn/09d@2x.png",
        'humidity': 78,
        'wind_speed': 4.9,
        'sunrise': datetime.fromtimestamp(1719381000).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719431400).strftime('%I:%M %p')
    },
    "Delhi": {
        'city': "Delhi",
        'country': "India",
        'temperature': 38,
        'temp_min': 34,
        'temp_max': 40,
        'description': "Hot and Sunny",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 25,
        'wind_speed': 4.0,
        'sunrise': datetime.fromtimestamp(1719382200).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719432600).strftime('%I:%M %p')
    },
    "Bengaluru": {
        'city': "Bengaluru",
        'country': "India",
        'temperature': 26,
        'temp_min': 22,
        'temp_max': 28,
        'description': "Partly Cloudy",
        'icon': "http://openweathermap.org/img/wn/02d@2x.png",
        'humidity': 65,
        'wind_speed': 5.0,
        'sunrise': datetime.fromtimestamp(1719384000).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719434400).strftime('%I:%M %p')
    },
    "Hyderabad": {
        'city': "Hyderabad",
        'country': "India",
        'temperature': 34,
        'temp_min': 30,
        'temp_max': 36,
        'description': "Sunny",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 40,
        'wind_speed': 4.8,
        'sunrise': datetime.fromtimestamp(1719382800).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719433200).strftime('%I:%M %p')
    },
   
"Lucknow": {
    'city': "Lucknow",
    'country': "India",
    'temperature': 35,
    'temp_min': 31,
    'temp_max': 37,
    'description': "Sunny",
    'icon': "http://openweathermap.org/img/wn/01d@2x.png",
    'humidity': 35,
    'wind_speed': 4.1,
    'sunrise': datetime.fromtimestamp(1719382200).strftime('%I:%M %p'),
    'sunset': datetime.fromtimestamp(1719432600).strftime('%I:%M %p')
},
    "Ahmedabad": {
        'city': "Ahmedabad",
        'country': "India",
        'temperature': 36,
        'temp_min': 32,
        'temp_max': 39,
        'description': "Hot and Sunny",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 28,
        'wind_speed': 4.3,
        'sunrise': datetime.fromtimestamp(1719382200).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719432600).strftime('%I:%M %p')
    },
    "Jaipur": {
        'city': "Jaipur",
        'country': "India",
        'temperature': 37,
        'temp_min': 33,
        'temp_max': 40,
        'description': "Sunny",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 30,
        'wind_speed': 4.7,
        'sunrise': datetime.fromtimestamp(1719382200).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719432600).strftime('%I:%M %p')
    },
    "Coimbatore": {
        'city': "Coimbatore",
        'country': "India",
        'temperature': 28,
        'temp_min': 25,
        'temp_max': 30,
        'description': "Partly Cloudy",
        'icon': "http://openweathermap.org/img/wn/02d@2x.png",
        'humidity': 60,
        'wind_speed': 4.0,
        'sunrise': datetime.fromtimestamp(1719382800).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719433200).strftime('%I:%M %p')
    },
    "Los Angeles": {
        'city': "Los Angeles",
        'country': "US",
        'temperature': 24,
        'temp_min': 20,
        'temp_max': 27,
        'description': "Sunny",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 50,
        'wind_speed': 3.2,
        'sunrise': datetime.fromtimestamp(1719393600).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719444600).strftime('%I:%M %p')
    },
    "Istanbul": {
        'city': "Istanbul",
        'country': "Turkey",
        'temperature': 22,
        'temp_min': 19,
        'temp_max': 25,
        'description': "Cloudy",
        'icon': "http://openweathermap.org/img/wn/04d@2x.png",
        'humidity': 63,
        'wind_speed': 4.5,
        'sunrise': datetime.fromtimestamp(1719385800).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719436200).strftime('%I:%M %p')
    },
    "Cairo": {
        'city': "Cairo",
        'country': "Egypt",
        'temperature': 35,
        'temp_min': 31,
        'temp_max': 38,
        'description': "Hot and Dry",
        'icon': "http://openweathermap.org/img/wn/01d@2x.png",
        'humidity': 20,
        'wind_speed': 3.8,
        'sunrise': datetime.fromtimestamp(1719384000).strftime('%I:%M %p'),
        'sunset': datetime.fromtimestamp(1719434400).strftime('%I:%M %p')
    }
}

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city').strip().title()
        if city in SAMPLE_WEATHER_DATA:
            weather_data = SAMPLE_WEATHER_DATA[city]
        else:
            weather_data = {'error': 'City not found in dataset!'}
    return render_template('index.html', weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)
