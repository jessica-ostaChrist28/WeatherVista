# WeatherVista

A simple web application for checking current weather conditions using the OpenWeatherMap API.

## Features

- Search for weather by city name
- Display current temperature, humidity, wind speed, and weather conditions
- Responsive web interface

## Prerequisites

- Python 3.7 or higher
- OpenWeatherMap API key (free tier available at [openweathermap.org](https://openweathermap.org/api))

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd WeatherVista
   ```

2. Create a virtual environment:

   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the root directory and add your OpenWeatherMap API key:
   ```
   API_KEY=your_api_key_here
   ```

## Usage

1. Run the application:

   ```
   python run.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/`

3. Enter a city name in the search box and click "Search" to view the current weather.

## Project Structure

```
WeatherVista/
├── run.py                 # Application entry point
├── requirements.txt       # Python dependencies
├── app/
│   ├── __init__.py        # Flask app factory
│   ├── routes.py          # Route definitions
│   ├── weather.py         # Weather API integration
│   ├── static/            # Static files (CSS, JS)
│   └── templates/         # HTML templates
│       └── index.html     # Main page template
└── README.md              # This file
```

## API Reference

This application uses the OpenWeatherMap Current Weather API. For more information, visit the [OpenWeatherMap API documentation](https://openweathermap.org/current).

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
