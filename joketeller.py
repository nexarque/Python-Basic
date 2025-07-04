import pyjokes               # imported the get joke module
import pyttsx3               # imported text to speech module

joke = pyjokes.get_joke()    # this is a function that gets jokes
print(joke)                  # this will print jokes

engine = pyttsx3.init()      # this will initialize the text to speech engine
engine.say(joke)             # this will connects the text to speech engine to the joke
engine.runAndWait()          # this will run the text to speech engine and wait for it to finish
