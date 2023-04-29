
import pyttsx3
engine = pyttsx3.init()
print( "Welcome to RoboSpeaker 1.1 created by Abhijit")
engine.setProperty('rate',120)
while True:
    x = input("Enter what you want me to pronounce : ")
    if x == "q":
        engine.say("bye bye friend")
        engine.runAndWait()
        break
    engine.say(x)
    engine.runAndWait()