# Import required modules:
import requests
import wikipedia as wk
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config


# Define function to find IP Address:
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

# Define function to search on Wikipedia:
def search_on_wikipedia(query):
    results = wk.summary(query, sentences=2)
    return results

# Define function to play on YouTube:
def play_on_youtube(video):
    kit.playonyt(video)

# Define function to search on Google:
def search_on_google(query):
    kit.search(query)

# Define function to provide information summary:
def find_info(topic, sentences=2):
    kit.info(topic)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+61{number}", message)

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

# Define function to send email:
def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False

NEWS_API_KEY = config("NEWS_API_KEY")

# Define function to obtain latest news:
def get_latest_news():
    news_headlines = []
    res = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]

OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")

# Define function to obtain weather report:
def get_weather_report(city):
    res = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

# Define function to obtain random joke:
def get_random_joke():
    headers = {
        'Accept': 'application/json'
        }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
# Define function to obtain random advice:
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']
    



