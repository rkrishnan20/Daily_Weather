import requests
import json


url = "https://api.openweathermap.org/data/2.5/weather?APPID=0cfeda5dd62fbac8495206d425ee1128&q=Washington,us&units=imperial"
r = requests.get(url)
# print(json.loads(r.content))
j = json.loads(r.content)

print('Hello, and welcome to the weather of the day here in ' + j["name"])
print('Let\'s get right into it, shall we?')

start = j["main"]["temp_min"]
now = j["main"]["temp"]
end = j["main"]["temp_max"]
main_weather = j["weather"][0]["main"]
weather_desc = j["weather"][0]["description"]

print('We\'re starting off at a temperature of ' + str(now) + ' F today.')

if now <= 32.0:
    print('Yeah, literally freezing, I know.')
    print('Up from ' + str(start) + ' F.')

    if abs(now - end) <= 10:
        print('And you know what else? We\'re going all the way up to a whopping ' + str(end) + ' F.')
elif now >= 45 and now <= 65:
    print('Kinda chilly, I guess, but not terrible.')
    print('Going up to a temperature of ' + str(end) + ' F.')
    
    if main_weather == 'Rain':
        print('A rain jacket and an umbrella are in order, but that\'s about it.')
else:    
    print('Oof. I don\'t envy you. Shorts & short-sleeved shirt weather, to say the least.')
    print('And carry a full water bottle with you--after all, Hydrate or Dydrate.')
