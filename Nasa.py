import requests
import cartopy.crs as ccrs 
import matplotlib.pyplot as plt
import os
from PIL import Image
import pyttsx3
import json
import webbrowser

Api_key = '3y53IxdmeCbXXqInKfo93tTdRMRiUa88903bgB7h'


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',173)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def NasaNews(Date):

    speak('connecting to the cloud....')

    Url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)

    Params = {'date':str(Date)}
    
    r = requests.get(Url,params = Params)

    Data = r.json()

    Info = Data['explanation']

    Title = Data['title']

    Image_Url = Data['url']

    Image_r = requests.get(Image_Url)

    FileName = str(Date) + '.jpg'

    with open(FileName,'wb') as f:

        f.write(Image_r.content)

    Path_1 = "C:\\Users\\ishwo\\Desktop\\Ai program\\" + str(FileName)

    Path_2 = "C:\\Users\\ishwo\\Desktop\\Ai program\\Nasa\\" + str(FileName)

    os.rename(Path_1, Path_2)

    img = Image.open(Path_2)

    img.show()

    print(Title)
    print(Info)
    speak(f"Title : {Title}" )
    speak(f'According to Space station : {Info}')

def MarsImage():

    name = 'curiosity' 

    date = '2022-05-15'

    Api_ = str('Api_Key')

    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{name}/photos?earth_date={date}&api_key={Api_key}"

    r = requests.get(url)

    Data = r.json()

    Photos = Data['photos'][:7]

    try:

        for index , photo in enumerate(Photos):

            camera = photo['camera']

            rover = photo['rover']

            rover_name = rover['name']

            camera_name = camera['name']

            full_camera_name = camera['full_name']

            date_of_photo = photo['earth_date']

            img_url = photo['img_src']

            p = requests.get(img_url)

            img = f'{index}.jpg'

            with open(img,'wb') as file:
                file.write(p.content)

            Path_1 = "C:\\Users\\ishwo\\Desktop\\Ai program\\"+ str(img)

            Path_2 = "C:\\Users\\ishwo\\Desktop\\Ai program\\Mars\\" + str(img)

            os.rename(Path_1,Path_2)

            os.startfile(Path_2)

            speak(f"This Image Was Captured With : {full_camera_name}")

            speak(f"On : {date_of_photo}")

    except:
        speak("There iS An Error!")
    
def IssTracker():

    url = "http://api.open-notify.org/iss-now.json"

    r = requests.get(url)

    Data = r.json()

    dt = Data['timestamp']

    lat = Data['iss_position']['latitude']

    lon = Data['iss_position']['longitude']

    speak('Tracking International Space station')

    print(f"Time And Date : {dt}")
    print(f"Latitude : {lat}")
    print(f"Longitude : {lon}")

    speak(f"Time And Date : {dt}")
    speak(f"Latitude : {lat}")
    speak(f"Longitude : {lon}")

    speak('The red marker shows the location of ISS above the surface of earth')

    plt.figure(figsize=(10,8))

    ax = plt.axes(projection = ccrs.PlateCarree())

    ax.stock_img()

    plt.scatter(float(lon),float(lat),color = 'red' , marker= 'o')

    plt.show()

def Astro(start_date,end_date):

    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={Api_key}"

    r = requests.get(url)

    Data = r.json()

    Total_Astro = Data['element_count']

    neo = Data['near_earth_objects']

    speak(f"Total Astroids Between {start_date} and {end_date} are : {Total_Astro}")

    speak("Exact Data For Those Astroids Are Listed Below .")

    for body in neo[start_date]:

        id = body['id']

        name = body['name']

        absolute = body['absolute_magnitude_h']

        print(id,name,absolute)
        speak({id})
        speak({name})
        speak({absolute})


def fetchAPOD(Date):
  url = "https://api.nasa.gov/planetary/apod"
 
  params = {
      'api_key':Api_key,
      'date':str(Date),
      'hd':'True'

  }

  response = requests.get(url,params=params)
  json_data = json.loads(response.text)
  image_url = json_data['hdurl']
  webbrowser.open(image_url)
  print(json_data)
  speak(json_data)