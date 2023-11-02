import json
import requests
import time
usr = input("Enter a city: ")
ApiKey = "2a3e506c612e2efa30d538d2f5201b76"


base_url = f"https://api.openweathermap.org/data/2.5/weather?q={usr}&appid={ApiKey}"

timeOfDay = None

x = requests.get(base_url)
wData = x.content

city = usr

# Your bytes-like object
data_bytes = wData
print(wData)

with open("data.txt", 'w') as file:
    file.write(str(wData))

with open("info.txt", 'a') as file:
    wData == file
# Decode the bytes and parse it as a JSON string

data_str = data_bytes.decode('utf-8')
data_dict = json.loads(data_str)
weather_info = data_dict['weather'][0]

main_description = weather_info['main']
timezone = data_dict['timezone']
description = weather_info['description']
sunset = data_dict['sys']['sunset']
sunrise = data_dict['sys']['sunrise']
#icon = weather_info['icon']

gmTime = time.gmtime()

print("\nMain Weather:", main_description,"| Description:", description)
print("Sunrise Time:", sunrise)
print("Sunset Time:", sunset)

print((time.time() - sunrise) // 3600)
hour = gmTime.tm_hour + timezone // 3600
print(str(hour)+"."+str(gmTime.tm_min))

for key in data_dict:
    print("")
    value = data_dict[key]
    #print(value)
