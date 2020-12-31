import pyautogui
import datetime
import subprocess
from googletrans import Translator
import os

def sshot():
    d = datetime.datetime.now()
    res_d=d.strftime('%D')
    res_date=res_d.replace('/','_')
    res_hour=d.strftime('%I')
    res_min=d.strftime('%M')
    res_second=d.strftime('%S')
    screenshot_name=res_date+' '+res_hour+' '+res_min+' '+res_second+'.png'
    image=pyautogui.screenshot()
    image.save('C:/Users/lenovo/Pictures/Screenshots/'+screenshot_name)


def datentime(query):
        d = datetime.datetime.now()
        if 'time' in query:
            res_time = d.strftime('%I')
            res_ap = d.strftime('%p')
            return 'its' + res_time + res_ap

        elif 'date' in query:
            res_month = d.strftime('%B')  # for month
            res_day = d.strftime('%A')
            res_day_no = d.strftime('%d')
            re_year = d.strftime('%Y')
            return 'its' + " " + res_day + " " + res_day_no + " " + res_month + " " + re_year
        elif 'wish' in query:
            res_wish = int(d.strftime('%H'))
            if res_wish < 12:
                return "good morning"
            elif 12 <= res_wish and res_wish < 16:
                return "good afternoon"
            else:
                return "good evening"



def openapps(query):
    if "open notepad" in query:
        subprocess.call("notepad.exe")
    elif "open calculator" in query:
        subprocess.call("calc.exe")
    elif "edge " in query:
        subprocess.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
    else:
        pass


def change_name(new_name):
    with open("name.txt", mode="w+") as go:
        name_change=go.read()
        go.write(new_name)

def remember_that(remember):
    with open("journal.txt",mode="w+") as thing:
        remembering=thing.read()
        thing.write(remember)

def translating(sentence, language,full_lang):
    try:
     if full_lang=='portuguese':
        translate = Translator()
        translate_process = translate.translate(sentence, dest='pt', src='en')
        print(translate_process.text)

     elif full_lang=='chinese':
        translate = Translator()
        translate_process = translate.translate(sentence, dest='zh-cn', src='en')
        print(translate_process.text)

     elif full_lang == 'spanish':
        translate = Translator()
        translate_process = translate.translate(sentence, dest='es', src='en')
        print(translate_process.text)

     elif full_lang=='bengali':
        translate = Translator()
        translate_process = translate.translate(sentence, dest='bn', src='en')
        print(translate_process.text)

     elif full_lang=='dutch':
        translate = Translator()
        translate_process = translate.translate(sentence, dest='nl', src='en')
        print(translate_process.text)

     elif full_lang=='punjabi':
        translate = Translator()
        translate_process = translate.translate(sentence, dest='pa', src='en')
        print(translate_process.text)

     elif full_lang=='turkish':
        translate = Translator()
        translate_process = translate.translate(sentence, dest='tr', src='en')
        print(translate_process.text)

     elif full_lang=='marathi':
        translate = Translator()
        translate_process = translate.translate(sentence, dest='mr', src='en')
        print(translate_process.text)
     else:
        translate=Translator()
        translate_process=translate.translate(sentence,dest=language,src='en')
        print(translate_process.text)
    except ValueError:
      print("Sorry not compatile with this language try something else")


def shutdown_process():
    os.system("shutdown /s /t 1")
    print("done")


