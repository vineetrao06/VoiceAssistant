# VoiceAssistant

A fully functional voice assistant that can handle many features and do several tasks for you - just with some simple voice commands. Tasks include: Playing music, drafting emails, sending tweets, and much more!

**Setup**:

- Install the dependencies using `pip install -r requirements.txt`
- If you're planning on using the bot to make tweets, make sure to create a [Twitter Developers Accunt](https://https://developer.twitter.com/en) if you haven't already.
- Additionally, you will need an [Open Weather Map Api](https://openweathermap.org) account to access the weather (All these accounts are free to create).
- Lastly, you will need to make a config.py document which will contain all the api keys, passwords, and email contacts. The format should look something like this:

  ```python
  #Find these api keys under your twitter developer account, and enter the values here:
  CONSUMER_KEY = 'your_twitter_api_keys'
  CONSUMER_SECRET = 'your_twitter_api_keys'
  ACCESS_KEY = 'your_twitter_api_keys'
  ACCESS_SECRET = 'your_twitter_api_keys'

  EMAIL_USERNAME = 'your_username'
  EMAIL_PASSWORD = 'your_password'

  #These are example contacts:
  #Strictly follow this format
  email_recipients = {
      #here is an example
      'John': ['johnsmith@gmail.com', 'John Smith'],
      'Bob': ['bobsmith@gmail.com', 'Bob Smith'],
  }

  WEATHER_API_KEY = "your_weather_api_key"
  ```

- You should be ready to go. Navigate to the directory and run the program by entering `python main.py` in your terminal.

Enjoy!
