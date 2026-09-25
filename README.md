# Weather Dashboard

A weather dashboard built with FastAPI, showing current conditions and a 5-day forecast for any city, using the OpenWeatherMap API.

## Features
- Real-time weather lookup by city name
- Current temperature, feels-like, humidity, and conditions
- 5-day forecast
- Clean, responsive UI

## Tech Stack
- **Backend:** Python, FastAPI, Uvicorn
- **External API:** OpenWeatherMap
- **Frontend:** HTML, CSS, Jinja2 templates

## Running Locally

\\\ash
git clone https://github.com/bandhavya2004/weather-dashboard-fastapi.git
cd weather-dashboard-fastapi
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
\\\

Create a \.env\ file with:
\\\
OPENWEATHER_API_KEY=your_api_key_here
\\\

Then run:
\\\ash
uvicorn main:app --reload
\\\

Open http://127.0.0.1:8000 in your browser.

## Live Demo
https://weather-dashboard-fastapi.onrender.com
