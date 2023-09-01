from flask import Flask, request, render_template
from ApplicationRejectionInterface import get_weather

app = Flask(__name__)
cities = [
    "mckinney,tx,us",
    "vijayawada,ap,in",
    "lake zurich,il,us",
    "tampa,fl,us",
    "san francisco,ca,us"
]

@app.route("/", methods=["GET"])
def index():
    temps = []
    for city in cities:
        data = get_weather(city)
        temps.append(data)
    print(temps)
    return render_template("index.html", temps=temps)

@app.route("/forecast", methods=["GET"])
def forecast():
    city = request.args.get("city")
    data = get_weather(city)
    return {
        "city": data["main"]["name"],
        "temp": data["main"]["temp"],
        #"data": data
    }