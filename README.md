# VoiceAssistant
 A fully functional chatbot that can handle many features and do several tasks for you - just with some simple voice commands. Tasks include: Playing music, drafting emails, sending twerets, and much more!

 Setup:

 - Install the dependencies using `pip install -r requirements.txt`
 - If you're planning on using the bot to make tweets, make sure to create a twitter developers accunt if you haven't already. You can find it [here](https://https://developer.twitter.com/en)
 - Additionally, you will need an [Open Weather Map Api](https://openweathermap.org) account to access the weather
 - Lastly, you will need to make a config.py document which will contain all the api keys, passwords, and email contacts. The format should look something like this:

 ```python
CONSUMER_KEY = 'your_keys'
CONSUMER_SECRET = 'your_keys'
ACCESS_KEY = 'your_keys'
ACCESS_SECRET = 'your_keys'

EMAIL_USERNAME = 'your_username'
EMAIL_PASSWORD = 'your_password'

#These are example contacts:
#Strictly follow this format
email_recipients = {
    'example': ['example@example.com', 'Full Name'],
    'Squidward': ['squidward@something.com', 'Squidward Tentacles'],
}

WEATHER_API_KEY = "e52d04faf9791cb59328bb593790255b"
 ```
