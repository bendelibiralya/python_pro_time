import speech_recognition as sr

def speech_eng():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say the word!")
        audio = r.listen(source, timeout=20)
    text = r.recognize_google(audio)
    return text

if __name__ == "__main__":
    # Burada fonksiyonu test edebilirsin
    print(speech_eng())

def speech_tr():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Birşey söyle!")
        audio = r.listen(source, timeout=20)
    text = r.recognize_google(audio, language="tr-TR")
    return text

