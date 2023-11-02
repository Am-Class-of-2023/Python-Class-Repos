import sky
import requests
import time

key = "fede235a503cc58fb3b9f354ddfcf9c9"
city = input("Enter a city: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"


def findItem(string):
    startIndex = content.find(string) + len(string) + 2
    endIndex = content[startIndex:].find(",") + startIndex
    Item = content[startIndex:endIndex]
    if "}" in Item: Item = Item[:-1]
    return Item

def getHour(tz):
    hour = hour + tz / 3600
    return hour

def findImage():
    if time >= 7 and time <= 8:
        return sky.dawn
    elif time > 8 and time < 19:
        return cloudy and sky.cloudy or sky.sunny
    elif time >= 19 and time <= 20:
        return sky.dusk
    else:
        return sky.night

response = requests.get(url)
content = str(response.content)
sunrise = int(findItem("sunrise"))
sunset = int(findItem("sunset"))
daytime = int(findItem("dt"))
timeZone = int(findItem("timezone"))
clouds = int(findItem("clouds\":{\"all"))


gmTime = time.gmtime()
hour = gmTime.tm_hour + timeZone // 3600
minute = gmTime.tm_min
time = hour + minute / 60
cloudy = clouds > 10

with open("data.txt","a") as data:
    data.write(f"""City: {city} at {hour}:{minute}\n
Cloudy: {cloudy}, {clouds} clouds\n
Time of day: {findImage()}
""")
    
img = findImage()
sky.openUrl(img)

findFile = input("Would you like to load data from file: ")
if findFile == "yes":
    city = input("Enter a city: ")
    intime = input("Enter a time: ")
    with open ("data.txt","r") as data:
        string = data.readlines()
        inp = f"City: {city} at {intime}\n"
        if inp in string:
            ind = string.index(inp)
            url = string[ind + 4][13:]
            sky.openUrl(url)

