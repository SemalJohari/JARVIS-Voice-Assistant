import os
import eel

from engine.features import *
from engine.command import *
from engine.auth import recognize
def start():
    
    eel.init("website")

    playAssistantSound()

    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recognize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello and Welcome, How can I Help You?")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")
            
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)