import pyautogui
import datetime
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