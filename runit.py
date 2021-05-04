import urllib, json

URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=400094&date=01-05-2021"

response = urllib.urlopen(url)
data = json.loads(response.read())
print data


