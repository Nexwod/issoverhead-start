import requests
from datetime import datetime
import smtplib

MY_LAT = 6.222004 # Your latitude
MY_LONG = 7.082116 # Your longitude

PASSWORD = "opjfhgonjoyxgupn"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunrise)
# print(sunset)
time_now = datetime.now()



#If the ISS is close to my current position
if iss_latitude > MY_LAT - 5 or iss_latitude < MY_LAT + 5 and iss_longitude > MY_LONG - 5 or iss_longitude < MY_LONG + 5:
    if sunset == time_now.hour:
    # with open()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="happinessjoseph065@gmail.com", password=PASSWORD)
            connection.sendmail(from_addr="happinessjoseph065@gmail.com", to_addrs="happinessjoseph@gmail.com", msg="subject: ISSOVERHEARD\n\n Look into the sky now, iss is over head you")

# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



