import speech_recognition as sr

earings=sr.Recognizer()
try:
    with sr.Microphone() as source:
        earings.adjust_for_ambient_noise(source)
        voice=earings.listen(source)
        text=earings.recognize_google(voice) #text=earings.recognize_google(voice,language="ml-IN")
        print(text)
except:
    pass