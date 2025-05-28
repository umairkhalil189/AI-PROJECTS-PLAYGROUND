import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk



engine = pyttsx3.init()

voices = engine.getProperty('voices')        #get details of current voices

for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.setProperty('rate', 150 )
   # engine.say('')
#engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content= ""
    while content == "":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("say something...\n")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language= 'en-in')
            print("Your Said = " + content )
        except Exception as e:
            print("Please say Again...")

    return content

def main_process():
    while True:    
        request = command().lower()
        if "hello" in request:
            speak("how can i help you.")
        elif "play music" in request:
            speak("playing music")
            song= random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=DkdMdNdCjbE")
            elif song ==2:
                webbrowser.open("https://www.youtube.com/watch?v=XO8wew38VM8")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=4tywp83zkmk") 
        elif "time" in request:
            now_time= datetime.datetime.now().strftime("%H : %M")
            print("Current time is: " + str(now_time))
            speak("Current time is: " + str(now_time))
        elif "date" in request:
            now_date= datetime.datetime.now().strftime("%d : %m : %y")
            print("Current date is: " + str(now_date))
            speak("Current date is: " + str(now_date))
        elif "new work" in request:
            task= request.replace("new work", "")
            task= task.strip()
            if task !="":
                speak("Adding Task: " + task)
                with open ("to_do.txt", "a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
            with open ("to_do.txt", "r") as file:
                speak("Work, we have to do today is: " + file.read())
        elif "show work" in request:
            with open ("to_do.txt", "r") as file:
                task = file.read()
                notification.notify(
                   title =  "Today's work",
                   message = task
                )
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")
        elif "delete work" in request:
            task= request.replace("delete work", "").strip()
            if task !="":
                try:
                    with open('to_do.txt', 'r') as file:
                        tasks= file.readlines()

                    with open("to_do.txt", 'w') as file:
                        found= False
                        for line in tasks:
                            if line.strip() != task:
                                file.write(line)
                            else:
                                found= True

                    if found:
                        speak(f"Deleted Task: {task}")
                    else:
                        speak("Task not Found.")

                except FileNotFoundError:
                    speak("To do list is Empty.")
        elif "wikipedia" in request:
            request = request.replace("jarvis", "")
            request = request.replace("search wikipedia ", "")
            result = wikipedia.summary(request, sentences=2)
            print(result)
            speak(result)
        elif "open youtube" in request:
            webbrowser.open("https://www.youtube.com")
        elif "search google" in request:
            request= request.replace("jarvis ", "")
            request = request.replace("search google", "")
            webbrowser.open("https://www.google.com/search?q=" + request)
        elif "send whatsapp" in request:
               pwk.sendwhatmsg("+010001000010", "anything :(  !!! ): abcc", 20, 12, 30)
              # time.sleep(5)
       # elif "send email" in request:
        #       pwk.send_mail("abc@gmail.com", "anything :(  !!! ): abccc", 20, 12, 30)
  
  
main_process()

    