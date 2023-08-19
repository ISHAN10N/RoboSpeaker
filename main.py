import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

if __name__ == '__main__':
    print("Welcome to RoboSpeaker!")

    while True:
        x = input("Enter what you want me to speak  ")
        if x == "q":
            break
        text = f"{x}"
        speak.Speak(text)
