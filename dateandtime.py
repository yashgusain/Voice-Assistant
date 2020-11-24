import datetime

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
        res_wish = d.strftime('%p')
        if 'AM' in res_wish:
            return "good morning"
        else:
            return "good night"
    else:
        pass