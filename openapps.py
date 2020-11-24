import subprocess


def openapps(query):
    if "open notepad" in query:
        subprocess.call("notepad.exe")
    elif "open calculator" in query:
        subprocess.call("calc.exe")
    elif "edge " in query:
        subprocess.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")


openapps("edge")
