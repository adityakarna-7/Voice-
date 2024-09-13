import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import psutil
import imdb
import webbrowser
import pywhatkit
import os
from keyboard import press_and_release
from keyboard import press
from requests import get, request
import webbrowser as web
import requests
from bs4 import BeautifulSoup
from playsound import playsound
from pywikihow import search_wikihow
from geopy.distance import great_circle # pip install geopy
from geopy.geocoders import Nominatim # pip install geopy
import webbrowser # pip install webbrowser
import geocoder # pip install geocoder
import bs4
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1                                           
        audio = r.listen(source,0,4)                                                                    

    try:                                                                    
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")

        return "None"
    return query

def Dateconverter(Query):

    Date = Query.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def GoogleMaps(Place):

    Url_Place = "https://www.google.com/maps/place/" + str(Place)

    geolocator = Nominatim(user_agent="myGeocoder")

    location = geolocator.geocode(Place , addressdetails= True)

    target_latlon = location.latitude , location.longitude

    webbrowser.open(url=Url_Place)

    location = location.raw['address']

    target = {'city' : location.get('city',''),
                #'state' : location.get('state',''),
                'country' : location.get('country','')}

    current_loca = geocoder.ip('me')

    current_latlon = current_loca.latlng

    distance = str(great_circle(current_latlon,target_latlon))
    distance = str(distance.split(' ',1)[0])
    distance = round(float(distance),2)

    speak(target)
    speak(f'{Place} is {distance} kilometres away from you')

def My_Location():

    speak("connecting to the cloud...")
    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' +ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    print(f'{state , country}')

    speak(f"Your current location is  {state , country}")

def Temp():
        search = "temperature in my current location"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div",class_ = "BNeawe").text
        speak(f"The Temperature Outside Is {temperature} ")

        speak("Do I Have To Tell You Another Place Temperature ?")
        next = takeCommand()

        if 'yes' in next:
            speak("Tell Me The Name Of tHE Place ")
            name = takeCommand()
            search = f"temperature in {name}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temperature = data.find("div",class_ = "BNeawe").text
            speak(f"The Temperature in {name} is {temperature}")

        else:
            speak("no problem sir")

def CoronaVirus(Country):

    countries = str(Country).replace(" ","")

    url = f"https://www.worldometers.info/coronavirus/country/{countries}/"

    result = requests.get(url)

    soups = bs4.BeautifulSoup(result.text,'lxml')

    corona = soups.find_all('div',class_ = 'maincounter-number')

    Data = []

    for case in corona:

        span = case.find('span')

        Data.append(span.string)

    cases , Death , recovered = Data
    print(cases)
    print(Death)
    print(recovered)

    speak(f"Cases : {cases}")
    speak(f"Deaths : {Death}")
    speak(f"Recovered : {recovered}")
    
def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open("C:\\Users\\ishwo\\Desktop\\Ai program\\Data.txt",'a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(term)

    pywhatkit.search(Query)

    os.startfile("C:\\Users\\ishwo\\Desktop\\Ai program\\Googleimage\\start.py")

def cpu():

    print("Number of cores in system",)
    speak('Number of cores in system')
    print(psutil.cpu_count())
    speak(psutil.cpu_count())
    
    speak('The cpu usage is:')
    speak(psutil.cpu_percent(1))

    

   
    speak('Calculated in percentage')
    speak(psutil.cpu_times_percent(1))

    

    print(psutil.getloadavg())
    speak('average CPU load:')
    speak(psutil.getloadavg())

    print(psutil.cpu_freq())
    speak('Cpu frequency:')
    speak(psutil.cpu_freq())
    
def search_movie():
    



    
        # gathering information from IMDb
        moviesdb = imdb.IMDb()
    
        # search for title
        text =  takeCommand()
    
        # passing input for searching movie
        movies = moviesdb.search_movie(text)
    
        speak("Searching for " + text)
        if len(movies) == 0:
            speak("No result found")
        else:
    
            speak("I found these:")
    
            for movie in movies:
    
                title = movie['title']
                year = movie['year']
                # speaking title with releasing year
                speak(f'{title}-{year}')
    
                info = movie.getID()
                movie = moviesdb.get_movie(info)
    
                title = movie['title']
                year = movie['year']
                rating = movie['rating']
                plot = movie['plot outline']
    
                # the below if-else is for past and future release
                if year < int(datetime.datetime.now().strftime("%Y")):
                    print(
                        f'{title}was released in {year} has IMDB rating of {rating}.\
                        The plot summary of movie is{plot}')
                    speak(
                        f'{title}was released in {year} has IMDB rating of {rating}.\
                        The plot summary of movie is{plot}')
                    break 
    
                else:
                    print(
                        f'{title}will release in {year} has IMDB rating of {rating}.\
                        The plot summary of movie is{plot}')
                    speak(
                        f'{title}will release in {year} has IMDB rating of {rating}.\
                        The plot summary of movie is{plot}')
                    break

def ChromeAuto(command):

    query = str(command)

    if 'new tab' in query:

        press_and_release('ctrl + t')

    elif 'close tab' in query:

        press_and_release('ctrl + w')

    elif 'new window' in query:

        press_and_release('ctrl + n')

    elif 'history' in query:

        press_and_release('ctrl + h')

    elif 'download' in query:

        press_and_release('ctrl + j')

    elif 'bookmark' in query:

        press_and_release('ctrl + d')

        press('enter')

    elif 'incognito' in query:

        press_and_release('Ctrl + Shift + n')

    elif 'switch tab' in query:

        tab = query.replace("switch tab ", "")
        Tab = tab.replace("to","")
        
        num = Tab

        bb = f'ctrl + {num}'

        press_and_release(bb)

    elif 'open' in query:

        name = query.replace("open ","")

        NameA = str(name)

        if 'youtube' in NameA:

            web.open("https://www.youtube.com/")

        elif 'instagram' in NameA:

            web.open("https://www.instagram.com/")

        else:

            string = "https://www." + NameA + ".com"

            string_2 = string.replace(" ","")

            web.open(string_2)









