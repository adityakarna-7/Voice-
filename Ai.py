import sys
from matplotlib.pyplot import draw
import pyttsx3
import pywhatkit
import speech_recognition as sr
import random
import webbrowser
import os
import wolframalpha
import requests
from requests import get
import datetime
import wikipedia
from bs4 import BeautifulSoup
import subprocess as sp
import bs4
import ctypes
import time
import pyautogui
from sketchpy import library as lib
from quote import quote
from Features import GoogleSearch
from Features import takeCommand
from geopy.geocoders import Nominatim             
from geopy import distance
import warnings
import ecapture as ec



warnings.filterwarnings('ignore')
engine  = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',173)


### API KEYS #####

NEWS_API_KEY = "e7913d73232247d9bcae6a7b2e19d350"
TMDB_API_KEY = '2a5f06f09e06d29b5982c6a1ab662c3b'
api_key = 'fc60c656a6ec8bb4043e23b8c7142206'

 

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
            query = r.recognize_google(audio, language='en-au')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)    
            print("Say that again please...")
            

            return "None"
        return query

def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]

def startup():
    speak("Initializing the cloud...")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment sir")
    speak('Updating the cloud configuration')
    speak("All drivers are up and running")
    speak("All systems have been activated")

def computational_intelligence(question):
    try:
        client = wolframalpha.Client('4H2PW2-GEUAUQP7R3')
        answer = client.query(question)
        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        return None

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:

        speak("GoodMorning sir!")

    elif hour>=12 and hour<18:
        speak("GoodAfternoon sir!")


    else:
        speak("GoodEvening sir!")


    speak("Please tell me how may I help you")






if __name__ == "__main__":
    from playsound import playsound
    playsound("start.wav")
    speak('how can i help you??')
    while True:
    # if 1:
        query = takeCommand().lower()

        from playsound import playsound
        playsound('beep.wav')

        

        if 'wikipedia' in query or 'tell me about' in query:
            
            speak('Searching for results...')
            query =query.replace("wikipedia"," ")
            query =query.replace('tell me about',"  ")
            results = wikipedia.summary(query, sentences=5)
            speak("Internet says ....")
            print(results)
            speak(results)
            break

        elif 'photo' in query or 'pic' in query:
            ec.capture(0,"frame", "frame.png")
            
        elif 'thank you' in query or 'thanks' in query:
            break

        elif 'no' in query:
            break

        elif "calculate" in query:
            question = query
            answer = computational_intelligence(question)
            speak('The answer is')
            speak(answer)
            break

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif "what is" in query or 'who is' in query :
                question = query
                answer = computational_intelligence(question)
                speak(answer)
                break

        elif "hello" in query:
                speak('Hello , Good to see you')
                speak('How may i help You?')

        elif 'search' in query:
            speak('Searching {query}')
            query = query.replace('search', '')
            pywhatkit.search(query)
            break

        elif 'price of' in query:
            query = query.replace('price of', '')
            query = "https://www.amazon.in/s?k=" + query[-1] 
            webbrowser.open(query)
            break

        elif 'resume' in query or 'pause' in query:
            pyautogui.press("playpause")
       

        elif 'next' in query:
            pyautogui.press("nexttrack")

        

        elif 'weather' in query:
            try:
                speak("Tell me the city name.")
                city = takeCommand()
                api = "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=eea37893e6d01d234eca31616e48c631"
                w_data = requests.get(api).json()
                weather = w_data['weather'][0]['main']
                temp = int(w_data['main']['temp'] - 273.15)
                temp_min = int(w_data['main']['temp_min'] - 273.15)
                temp_max = int(w_data['main']['temp_max'] - 273.15)
                pressure = w_data['main']['pressure']
                humidity = w_data['main']['humidity']
                visibility = w_data['visibility']
                wind = w_data['wind']['speed']
                sunrise = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunrise'] + 19800))
                sunset = time.strftime("%H:%M:%S", time.gmtime(w_data['sys']['sunset'] + 19800))

                all_data1 = f"Condition: {weather} \nTemperature: {str(temp)}°C\n"
                all_data2 = f"Minimum Temperature: {str(temp_min)}°C \nMaximum Temperature: {str(temp_max)}°C \n" \
                            f"Pressure: {str(pressure)} millibar \nHumidity: {str(humidity)}% \n\n" \
                            f"Visibility: {str(visibility)} metres \nWind: {str(wind)} km/hr \nSunrise: {sunrise}  " \
                            f"\nSunset: {sunset}"
                speak(f"Gathering the weather information of {city}...")
                print(f"Gathering the weather information of {city}...")
                print(all_data1)
                speak(all_data1)
                print(all_data2)
                speak(all_data2)
            
            except Exception as e:
                pass
            break

        elif 'temperature' in query:
            from Features import Temp
            Temp()
            break

        elif 'play' in query:
                speak('Surfing the browser.... Hold on sir') 
                query = query.replace('friday'," ")  
                query = query.replace('play'," ")
                web = 'https://www.youtube.com/results?search_query=' + query
                pywhatkit.playonyt(query)
                speak(' Enjoy the music... ')
                break

        elif 'open facebook' in query:
                speak('alright sir...')
                webbrowser.open("https://www.facebook.com")
                speak('Shall I readout the messages too ?')
                break

        elif 'game' in query:
            from game import game_play
            game_play()
            break

        elif "trending" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            print(*get_trending_movies(), sep='\n')
            break

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "who am i" in query:
            speak("If you talk then definitely you are a human.")

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            break

        elif "don't listen" in query or "stop listening" in query:
                speak("for how much time you want to stop jarvis from listening commands")
                a = int(takeCommand())
                time.sleep(a)
                print(a)

        elif "advice" in query:
            speak(f"Here's an advice for you sir")
            advice = get_random_advice()
            speak(advice)
            print(advice)
            break

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)
            break

        elif 'Male or female' in query:
            speak('Nice question, But i will ignore that')

        elif 'tell me news' in query:
            speak(f"I'm reading out the latest news headlines sir")
            print(*get_latest_news(), sep='\n')
            speak(get_latest_news())
            break

        elif 'shutup' in query:
            sys.exit()

        elif "ip address" in query:
            ip = get("https://api.ipify.org").text
            print(f'{ip}')
            speak(f'Your current ip address is {ip}')
            break

        elif 'cpu' in query:
            from Features import cpu
            cpu()
            break
    
        elif 'quote' in query or 'quotes' in query:
            speak("Tell me the author or person name.")
            q_author = takeCommand()
            quotes = quote(q_author)
            quote_no = random.randint(1, len(quotes))
            # print(len(quotes))
            # print(quotes)
            print("Author: ", quotes[quote_no]['author'])
            print("-->", quotes[quote_no]['quote'])
            speak(f"Author: {quotes[quote_no]['author']}")
            speak(f"He said {quotes[quote_no]['quote']}")
            break


        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'mute volume' in query:
            pyautogui.press("volumemute")

        elif 'next' in query:
            pyautogui.press('next')

        elif "screenshot" in query:
            im = pyautogui.screenshot()
            im.save("ss.jpg")
            speak("screenshot has been taken")
            
        
        elif 'how to' in query:
            speak('Searching for best results.....')
            op = query.replace("jarvis","   ")
            max_result = 1
            from pywikihow import search_wikihow
            how_to_func = search_wikihow(op,max_result)
            assert len (how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)
             

        elif 'where is' in query:
            from Features import GoogleMaps
            Place = query.replace('where is' ,"  ")
            Place = Place.replace("cortana", "  ")
            GoogleMaps(Place)
            

###### CHATBOT###################################

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
            ans_q = random.choice(stMsgs)
            speak(ans_q)  
            ans_take_from_user_how_are_you = takeCommand()
            if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                speak('okey..')  
            elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                speak('oh sorry..')  
        elif 'make you' in query or 'created you' in query or 'develop you' in query:
            ans_m = " For your information eligo Created me ! I give Lot of Thannks to Him "
            print(ans_m)
            speak(ans_m)
        elif "who are you" in query or "about you" in query or "your details" in query:
            about = "I am friday an A I based computer program but i can help you lot like a your close friend ! i promise you ! Simple try me to give simple command ! like playing music or video from your directory i also play video and song from web or online ! i can also entain you i so think you Understand me ! ok Lets Start "
            print(about)
            speak(about)
        elif "hello" in query or "hello friday" in query:
            hel = "Hello Sir ! How May i Help you.."
            print(hel)
            speak(hel)
        elif "your name" in query or "sweat name" in query:
            na_me = "Thanks for Asking my name my self ! friday"  
            print(na_me)
            speak(na_me)
        elif "you feeling" in query:
            print("feeling Very sweet after meeting with you")
            speak("feeling Very sweet after meeting with you")

        
    
 #######################################################   

        
        elif 'space news' in query:
                speak('Say the date separated by And')

                Date = takeCommand()
                from Features import Dateconverter
                value = Dateconverter(Date)
                from Nasa import NasaNews
                NasaNews(value)  

        elif 'picture of' in query:
            speak ('Say the date sir..')
            Date = takeCommand()
            from Features import Dateconverter
            value = Dateconverter(Date)
            from Nasa import fetchAPOD
            fetchAPOD(value)

        elif 'my location' in query:
            from Features import My_Location
            My_Location()
            

        elif 'iron man' in query or 'tony' in query:
            obj = lib.rdj()
            obj.draw()

        elif 'spiderman' in query or 'tom holland' in query:
            obj = lib.tom_holland
            obj.draw()

        

        elif 'cases' in query:

            from Features import CoronaVirus

            speak("Which Country's Information would you like?")

            cccc = takeCommand()

            CoronaVirus(cccc)

        elif 'images' in query:

            from Nasa import MarsImage

            MarsImage()

        elif 'space station' in query:

            from Nasa import IssTracker

            IssTracker()

        elif'movie' in query:
            speak('what is the movie name?')
            from Features import search_movie
            search_movie()

        elif 'shutdown the laptop' in query:
                import os
                os.system('shutdown /s /t 0')

        break


        