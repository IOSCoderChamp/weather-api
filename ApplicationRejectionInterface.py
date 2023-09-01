import requests

url = "https://api.openweathermap.org/data/2.5/weather"
key = "d056742516a8c9d16439d38de2ab6987"
def get_weather(city):
    query = url + f"?q={city}&appid={key}&units=imperial" 
    response = requests.get(query)
    if response.status_code == 200:
        return response.json()
    else:
        return response.status_code