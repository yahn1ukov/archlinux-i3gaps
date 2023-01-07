import requests

CITY = ""
API_KEY = ""
UNITS = "Metric"
UNIT_KEY = "°C"

REQ = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units={}".format(CITY, API_KEY, UNITS))

try:
    if REQ.status_code == 200:
        TEMP = int(float(REQ.json()["main"]["temp"]))
        print("{} {}".format(TEMP, UNIT_KEY))
    else:
        print("")
except:
    print("")

