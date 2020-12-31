from win10toast import ToastNotifier
import time
import threading
import texttospeech as ttos

h = "remind me after 5 hour 3 min"
conversion = list(h.split(" "))
# for hour
reminding_time_hour = int(conversion[3])
frm_hr_t_sec = reminding_time_hour*1
# for minutes
reminding_time_minutes = int(conversion[5])
frm_min_sec = reminding_time_hour*1
# for hour and  minutes
reminding_hm = int(conversion[3])
reminding_mh = int(conversion[5])
reminding_time_hour_minutes=(frm_hr_t_sec+frm_min_sec)
def remind(finto_sec):
    to = ToastNotifier()
    time.sleep(finto_sec)
    to.show_toast("bello", duration=3)


if "hour" in h:
    background_task = threading.Thread(target=remind, args=[frm_hr_t_sec])
    background_task.start()
    ttos.speak("reminder set for hour")


elif "min " in h:
    background_task = threading.Thread(target=remind, args=[frm_min_sec])
    background_task.start()
    ttos.speak("reminder set for minutes")


elif "hour " in h and "min" in h:
    
    background_task = threading.Thread(target=remind, args=[frm_hm_t_sec])
    background_task.start()
    ttos.speak("reminder set for haour and min")
