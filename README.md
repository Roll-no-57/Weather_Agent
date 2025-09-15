# 🌦️ AI-Powered Weather Agent

An intelligent weather assistant powered by Google's Gemini AI and the ReAct (Reasoning and Acting) framework. This application provides natural language weather information using real-time data from Open-Meteo APIs.

## 🚀 Features

- **Natural Language Processing**: Ask questions in plain English like "Will it rain tomorrow in London?"
- **Comprehensive Weather Data**: Temperature, precipitation, wind, humidity, and more
- **Global Coverage**: Weather information for any location worldwide
- **Time-aware**: Handles queries about current weather, forecasts, and historical data
- **RESTful API**: Clean Flask-based API for integration
- **ReAct Agent**: Intelligent reasoning and tool use for complex queries
- **Deployment Ready**: Configured for easy deployment on Render

## 🏗️ Architecture

The application uses a sophisticated ReAct (Reasoning and Acting) agent architecture:

```
User Query → WeatherAgent → ReactAgent → Weather Tools → External APIs
                ↓
          Natural Language Response
```

### Core Components

- **WeatherAgent**: Main orchestrator that processes weather queries
- **ReactAgent**: Implements ReAct framework for reasoning and tool selection
- **Weather Tools**: Specialized functions for different weather operations
- **API Integration**: Connects to Open-Meteo for weather data and Geoapify for location services

## 📡 API Endpoints

### POST `/weather`
Process natural language weather queries.

**Request:**
```json
{
  "query": "What's the weather like in Paris tomorrow?"
}
```

**Response:**
```json
{
  "response": "Tomorrow in Paris, expect partly cloudy skies with a high of 22°C and a low of 15°C. There's a 20% chance of rain in the afternoon.",
  "sentiment": 0.0
}
```

### GET `/health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy"
}
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Local Development

1. **Clone the repository:**
```bash
git clone <repository-url>
cd Weather-Agent-main
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set environment variables:**
```bash
# Windows
set GEMINI_API_KEY=your_gemini_api_key_here

# Linux/macOS
export GEMINI_API_KEY=your_gemini_api_key_here
```

4. **Run the application:**
```bash
python app.py
```

5. **Test the API:**
```bash
curl -X POST http://localhost:5000/weather \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the weather in New York?"}'
```

### Alternative CLI Interface

For interactive testing, you can use the command-line interface:

```bash
python we_main.py
```

## 🚀 Deployment

### Render Deployment (Recommended)

This project includes `render.yaml` for easy deployment:

1. **Push to GitHub**
2. **Connect to Render:**
   - Go to [render.com](https://render.com)
   - Create new Web Service
   - Connect your GitHub repository
3. **Configure Environment:**
   - Set `GEMINI_API_KEY` in Render dashboard
4. **Deploy:** Render will automatically build and deploy

### Manual Deployment

```bash
# Install production dependencies
pip install -r requirements.txt

# Run with Gunicorn
gunicorn -w 2 -k gthread -b 0.0.0.0:$PORT app:app
```

## 📁 Project Structure

```
Weather-Agent/
├── app.py                 # Flask API application
├── weather_main.py        # Main WeatherAgent class
├── planning_agent.py      # ReAct agent implementation
├── weather_tools.py       # Weather-specific tools
├── tool.py               # Tool framework and decorators
├── we_main.py            # CLI interface (optional)
├── database.py           # Deprecated (can be deleted)
├── requirements.txt      # Python dependencies
├── render.yaml          # Deployment configuration
└── utils/
    ├── completions.py   # LLM interaction utilities
    ├── extraction.py    # XML tag parsing
    ├── logging.py       # Logging utilities (optional)
    └── __init__.py      # Package marker
```

### File Descriptions

#### Core Files
- **`app.py`**: Flask web application with REST API endpoints
- **`weather_main.py`**: Contains the main `WeatherAgent` class that orchestrates weather queries
- **`planning_agent.py`**: Implements the ReAct (Reasoning and Acting) agent framework
- **`weather_tools.py`**: Collection of weather-related tools (date parsing, location lookup, weather data fetching)
- **`tool.py`**: Framework for creating and managing tools with type validation

#### Utility Files
- **`utils/completions.py`**: Handles interactions with the Gemini language model
- **`utils/extraction.py`**: Parses XML tags from agent responses
- **`utils/logging.py`**: Decorative logging functions (optional)

#### Configuration Files
- **`requirements.txt`**: Python package dependencies
- **`render.yaml`**: Render.com deployment configuration

#### Optional Files
- **`we_main.py`**: Command-line interface for interactive testing
- **`database.py`**: Deprecated database module (safe to delete)

## 🔧 Weather Tools

The agent has access to these specialized tools:

### Date & Time Tools
- `get_current_datetime()`: Current date and time
- `parse_date_time()`: Parse natural language date references
- `calculate_date()`: Calculate dates with offsets
- `get_current_year()`: Current year
- `get_current_month()`: Current month

### Location Tools
- `get_location_coordinates()`: Convert location names to coordinates
- `get_current_location_from_ip()`: Detect user location from IP

### Weather Data Tools
- `get_weather_forecast()`: Current and future weather data
- `get_historical_weather()`: Past weather data

## 🌡️ Supported Weather Variables

### Daily Variables
- Temperature: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`
- Sun: `sunrise`, `sunset`, `daylight_duration`, `sunshine_duration`
- Precipitation: `precipitation_sum`, `rain_sum`, `snowfall_sum`
- Wind: `wind_speed_10m_max`, `wind_gusts_10m_max`
- General: `weather_code`, `precipitation_probability_max`

### Hourly Variables
- Temperature: `temperature_2m`, `apparent_temperature`, `dew_point_2m`
- Humidity: `relative_humidity_2m`
- Precipitation: `precipitation_probability`, `precipitation`, `rain`, `snowfall`
- Wind: `wind_speed_10m`, `wind_direction_10m`, `wind_gusts_10m`
- Atmospheric: `surface_pressure`, `cloud_cover`

### Current Variables (Real-time)
- `temperature_2m`, `relative_humidity_2m`, `apparent_temperature`
- `precipitation`, `rain`, `wind_speed_10m`, `weather_code`
- `is_day` (day/night indicator)

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Google Gemini API key | Yes |
| `PORT` | Server port (default: 5000) | No |
| `PYTHONUNBUFFERED` | Python output buffering | No |

### Model Configuration

The default model is `gemini-1.5-flash`. You can modify this in `app.py`:

```python
agent = WeatherAgent(model="your-preferred-model")
```

## 🧪 Example Queries

The agent can handle various types of weather queries:

### Basic Weather
- "What's the weather today?"
- "Current temperature in Tokyo"
- "Is it raining in London?"

### Location-specific
- "Weather in New York tomorrow"
- "Temperature in Mumbai this morning"
- "Will it snow in Moscow this weekend?"

### Time-specific
- "Weather forecast for next week"
- "Was it sunny yesterday in Paris?"
- "Temperature 3 days ago in Berlin"

### Complex Queries
- "Should I carry an umbrella this afternoon?"
- "Compare today's weather with tomorrow in Dubai"
- "What's the humidity level in Singapore right now?"

## 🐛 Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   Error: GEMINI_API_KEY not configured
   ```
   **Solution**: Set the `GEMINI_API_KEY` environment variable

2. **Location Not Found**
   ```
   Error: Location 'XYZ' not found
   ```
   **Solution**: Try using a more specific location name or coordinates

3. **Network Errors**
   ```
   Error fetching weather data
   ```
   **Solution**: Check internet connection and API service status

### Debug Mode

Enable debug mode for development:

```python
app.run(debug=True)
```

## 🔒 Security Considerations

- Keep your `GEMINI_API_KEY` secret and never commit it to version control
- Use environment variables for sensitive configuration
- Consider rate limiting for production deployments
- Validate user inputs to prevent abuse



## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [Open-Meteo](https://open-meteo.com/) for weather data
- [Google Gemini](https://deepmind.google/technologies/gemini/) for AI capabilities
- [Geoapify](https://www.geoapify.com/) for location services
- [ReAct Framework](https://arxiv.org/abs/2210.03629) for reasoning methodology

---

**Built with ❤️ using AI and modern weather APIs**
