import requests
from datetime import datetime as dt
from twilio.rest import Client


api_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "463bdb85599cb329700c8e5a5da65610"
account_sid = 'AC6a0771bb1bde94d1ff6e192df79346be'
auth_token = '98be4f58336eafd9a7ec2209888a855b'

weather_parameters = {
    "lat": 5.606120,
    "lon": -0.249737,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

current_hour = dt.now().hour
response = requests.get(api_endpoint, params=weather_parameters)
response.raise_for_status()
weather_today = response.json()

will_rain = False
forecast_slice = weather_today["hourly"][6:22]
for hour_data in forecast_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to carry an umbrella",
        from_='+17722223396',
        to='+233549583848'
    )
    print(message.status)
