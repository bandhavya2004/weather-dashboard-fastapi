from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

API_KEY = os.environ.get("OPENWEATHER_API_KEY")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html", {"weather": None})

@app.post("/", response_class=HTMLResponse)
def get_weather(request: Request, city: str = Form(...)):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        return templates.TemplateResponse(request, "index.html", {"weather": None, "error": "City not found"})

    weather = {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
    }

    forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    forecast_response = requests.get(forecast_url)
    forecast_data = forecast_response.json()

    forecast = []
    if forecast_data.get("cod") == "200":
        seen_dates = set()
        for entry in forecast_data["list"]:
            date = entry["dt_txt"].split(" ")[0]
            time = entry["dt_txt"].split(" ")[1]
            if time == "12:00:00" and date not in seen_dates:
                seen_dates.add(date)
                forecast.append({
                    "date": date,
                    "temp": entry["main"]["temp"],
                    "description": entry["weather"][0]["description"],
                })

    return templates.TemplateResponse(request, "index.html", {"weather": weather, "forecast": forecast})
