from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib

import tweepy
import credentials

import requests
import json

from pygame import mixer
from time import sleep

auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY,
                           credentials.CONSUMER_SECRET)
auth.set_access_token(credentials.ACCESS_KEY, credentials.ACCESS_SECRET)
api = tweepy.API(auth)


def computerSay(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


def userCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am ready to talk")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("You said: " + command + "\n")

    except sr.UnknownValueError:
        command = userCommand();

    return command.lower()

# if statements for executing commands


def assistant(command):

    if "what's up" in command:
        computerSay('Chillin\' dawg')

    elif 'send' and 'tweet' in command:
        tweet()

    elif 'email' in command:
        email()

    elif 'open subreddit' in command:
        openSubreddit(command)

    elif 'weather' in command:
        findWeather()

    elif 'shut up' in command:
        computerSay('no u')

    elif 'meme' in command:
        generateMeme()

    elif 'play' and 'song' in command:
        playSong()
    
    elif 'open website' in command:
        openWebsite(command)


def openWebsite(command):
    reg_ex = re.search('open website (.+)', command)
    if reg_ex:
        domain = reg_ex.group(1)

    else:
        computerSay('Which website do you want to open?')
        domain = userCommand()

    url = 'https://www.' + domain
    webbrowser.open(url)
    print('Done!')

def openSubreddit(command):
    reg_ex = re.search('open website (.+)', command)

    if reg_ex:
        subreddit_name = reg_ex.group(1)

    else:
        computerSay('Which subreddit do you want to open?')
        subreddit_name = userCommand()
    
    base_url = 'https://www.reddit.com/r/'
    subreddit_name = subreddit_name.replace(" ", "") #takes away spaces
    computerSay('Got it')
    subreddit_link = base_url + subreddit_name

    webbrowser.open(subreddit_link)

 
def tweet():
    computerSay('Do you want anyone tagged in the tweet?')

    want_tagged = userCommand().lower()

    all_tagged_ppl = []

    if 'yes' in want_tagged:
        computerSay('Who do you want tagged?')

        while True:
            person_tagged = userCommand()

            person_tagged = person_tagged.replace(" ", "")  # takes away spaces

            # puts "@" to the start of the name
            person_tagged = ''.join(('@', person_tagged))

            # adds spacing between tagged people and appends it to the list of tagged ppl
            all_tagged_ppl.append(person_tagged + ' ')

            print(all_tagged_ppl)

            computerSay('Do you want anyone else? Yes or no?')
            anyone_else = userCommand().lower()

            if 'no' in anyone_else:
                computerSay('Got it')
                break

            elif 'yes' in anyone_else:
                computerSay('Okay')

            else:
                computerSay("I'll take that as a no")
                break

            computerSay('Who else?')

    elif 'no' in want_tagged:
        computerSay('Okay, then')

    computerSay('What do you want the tweet to say?')

    tweet_content = userCommand()

    amnt_ppl_tagged = len(all_tagged_ppl)

    if (amnt_ppl_tagged >= 1):
        for i in range(0, amnt_ppl_tagged):
            tweet_content = ''.join((all_tagged_ppl[i], tweet_content))

    print(tweet_content)

    api.update_status(tweet_content)  # finally sends the tweet

    computerSay('Tweet sent')


def email():
    computerSay('Who is the recipient?')
    recipient = userCommand().lower()

    for person in credentials.email_recipients:
        if person in recipient:
            computerSay('What should I say?')
            content = userCommand()

            # init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            # identify to server
            mail.ehlo()

            # encrypt session
            mail.starttls()

            # login
            mail.login(credentials.EMAIL_USERNAME, credentials.EMAIL_PASSWORD)

            # send message

            mail.sendmail(
                credentials.email_recipients[person][1], credentials.email_recipients[person][0], content)

            # end mail connection
            mail.close()

            computerSay('Email sent.')

    if person not in recipient:
        computerSay('I don\'t know what you mean!')


computerSay('I am ready for your command')


def findWeather():
    computerSay('Give me a city name:')

    city_name = userCommand()
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # complete_url variable to store
    # complete url address
    complete_url = f"{base_url}appid={credentials.WEATHER_API_KEY}&q={city_name}&units=imperial"

    # get method of requests module
    # return response object
    response = requests.get(complete_url).json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if response["cod"] != "404":
        main = response['main']
        computerSay(
            f"Currently, {response['name']}'s weather is at {round(main['temp'])} degrees. Would you like to know more?")

        want_to_know_more = userCommand()

        if 'yes' in want_to_know_more:
            computerSay(
                f"{response['name']}'s humidity is at {main['humidity']}%' and the cloud description is {response['weather'][0]['description']}")

        elif 'no' in want_to_know_more:
            computerSay('Okay')

        else:
            computerSay("I'll take that as a no")
    else:
        computerSay("City Not Found ")

def playSong():
    computerSay("Playing a song.. Say stop to pause")
    mixer.init()
    mixer.music.load('song.mp3')
    mixer.music.play()
    wanna_stop = userCommand()

    if 'stop' in wanna_stop:
        print('Stopping...')
        mixer.music.stop()

def generateMeme():
    response = requests.get('https://meme-api.herokuapp.com/gimme').json()
    url = response['url']
    webbrowser.open(url)
    computerSay('There! You happy?')

while True:
    assistant(userCommand())
