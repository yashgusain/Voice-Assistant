import threading
from win10toast import ToastNotifier
import time
lol=5
time_=int(lol)
def no(lo):
    to=ToastNotifier()
    time.sleep(10)
    to.show_toast("helo",duration=lo)
b = threading.Thread(target=no,args=[time_])
b.start()
print("task done")
