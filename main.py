import requests
import os
from twilio.rest import Client


account_sid = "Your-sid"
auth_token = "Your-auth"

API_KEY="Your-api-key"
site="https://api.openweathermap.org/data/2.5/onecall"
Latitude=12.9178626
Longitude=77.5908738
params_1={

    "lat":Latitude,
    "lon":Longitude,
    "exclude":"current,minutely,daily",
    "appid":API_KEY,


}

request=requests.get(site,params=params_1)
request.raise_for_status()
data=request.json()

hourly=data["hourly"][:12]



will_rain=False
for hours in range(len(hourly)):
    condition_code = data["hourly"][:12][hours]['weather'][0]["id"]
    if int(condition_code)<700:
        will_rain=True


if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain cow☔☔",
        from_='Your twilio no',
        to='Your no',
    )
    print(message.status)






