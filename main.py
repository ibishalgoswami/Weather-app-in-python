import time
import re
from googletrans import Translator
import requests
import speech_recognition as sr
#from pprint import pprint(To print the data as a json format)

# Creating custom exception

class langexxp(Exception):
   def __init__(self, message):
       self.message = message

# choosing the language
try:
   langinp = input('Choose your language first Bengali Hindi Or English')
   if langinp == "bengali" or langinp == "Bengali":
       language = "bn-IN"
   elif langinp == "hindi" or langinp == "Hindi":
       language = "hi-IN"
   elif langinp == "english" or langinp == "English":
       language = "en"
   else:
       raise langexxp("Choose any above language before proceeding")

except langexxp as e:
   print(e.message)
   exit()

# Using of speech recognition technique for recognizing the city.
r = sr.Recognizer()
with sr.Microphone() as source:
   # listen for 5 seconds and create the ambient noise energy level
   r.adjust_for_ambient_noise(source, duration=6)
   print("Welcome to Weather Forecasting app,which city you are looking for")
   audio = r.listen(source)
   print("time over")

try:
   text = r.recognize_google(audio, language="en")
   print(text)

except:
   pass

# Gathering the data from the weather api
try:
   city = text
   url = 'http://api.openweathermap.org/data/2.5/weather?q={}&APPID=fdaf79681b7bf4b1eb32a7ccef7b814f&units=metric'.format(
       city)
   res = requests.get(url)
   data = res.json()
   # pprint(data)
   temp = data['main']['temp']
   weather = data['weather'][0]['description']
   humidity = data['main']['humidity']
   sunrise = data['sys']['sunrise']
   sunset = data['sys']['sunset']
   windspeed = data['wind']['speed']
   res_sunrise = time.ctime(sunrise)
   res_sunset = time.ctime(sunset)

except:
   print("Choose your City Please")
   exit()

# creating a function which handles all the queries

def query():

   try:
       # Using of speech recognition technique
       r = sr.Recognizer()
       with sr.Microphone() as source:
           # listen for 3 seconds and create the ambient noise energy level
           r.adjust_for_ambient_noise(source, duration=8)
           print("\n")
           print("Say your query about the weather here")
           audio = r.listen(source)
           print("time over")

       try:
           query = r.recognize_google(audio, language=language)
           print(query)

       except:
           pass

       # Using of google translator
       translator = Translator()
       translations = translator.translate([query], dest='en')
       for translation in translations:
           query = translation.text
           query = query.lower()
           print(query)

       res = query.find("temp")
       res1 = query.find("temperature")
       res2 = query.find("weather")
       res3 = query.find("humidity")
       res4 = query.find("sunrise")
       res5 = query.find("sunset")
       res6 = query.find("sun rise")
       res7 = query.find("rising")
       res8 = query.find("risen")
       res9 = query.find("settle down")
       res10 = query.find("wind speed")
       res11 = query.find("wind")

       if res >= 0 or res1 >= 0:
           result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', query)
           print(f"Today's Temperature in {city} is", temp, "°C")

       elif res2 >= 0:
           result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', query)
           print(f"Weather in {city} is", weather)

       elif res3 >= 0:
           result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', query)
           print(f"humidity in {city} is", humidity)

       elif res4 >= 0 or res6 >= 0 or res7 >= 0 or res8 >= 0:
           result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', query)
           print(f"Today Sun rising time in {city}", res_sunrise)

       elif res5 >= 0 or res9 >= 0:
           result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', query)
           print(f"Today Sun set time in {city}", res_sunset)

       elif res10 >= 0 or res11 >= 0:
           result = re.findall(r'[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?', query)
           print(f"Today wind speed in {city}", windspeed,"m/s")
       else:
           print("Your query cannot be found")

   except:
       print("your searched query cannot be found")

# Calling the query handling function.

query()

while True:

   # Getting input from the user and try to execute the function on the basic of user input.
   try:
       inp = input('Do you want to Continue YES! OR NO\n')
       if inp == 'NO' or inp == 'No' or inp == 'no':
           break
       else:
           query()
   except:
       print("Invalid input")