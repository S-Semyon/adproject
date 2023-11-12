import datetime
import time
import keyboard
from playsound import playsound

def change_time(time: str = 0):
    pass

def stope():
    t1.s = 1


class Date:
    def __init__(self, setting):
        self.date = setting
        l = list(self.date.split())
        l = l[0].split('-') + l[1].split(':')
        self.year = int(l[0])
        self.month = int(l[1])
        self.day = int(l[2])
        self.hour = int(l[3])
        self.min = int(l[4])
        self.sec = int(l[5])
        self.s = 0
        self.allsec = self.day * 3600 * 24 + self.hour * 3600 + self.min * 60 + self.sec
        self.ost = self.allsec

    def summa(self):
        l = list(str(datetime.datetime.now())[:-7].split())
        l = l[0].split('-') + l[1].split(':')
        year = int(l[0])
        month = int(l[1])
        day = int(l[2])
        hour = int(l[3])
        min = int(l[4])
        sec = int(l[5]) + self.ost
        j = 0
        while j == 0:
            if sec >= 60:
                min += 1
                sec -= 60
            elif min >= 60:
                hour += 1
                min -= 60
            elif hour >= 24:
                day += 1
                hour -= 24
            else:
                j = 1

        self.dateb = str(year) + '-' + str(month) + '-' + str(day) + ' ' + str(hour) + ':' + str(min) + ':' + str(sec)



class Timer:
    def __init__(self):
        pass


    def start_timer(self, t1):
        j = 0
        t1.summa()
        print(t1.dateb)
        while j <= t1.ost and t1.s == 0:
            time.sleep(1)
            j += 1
            change_time()
            keyboard.add_hotkey('Ctrl + s + 1', stope)
        if t1.s == 1:
            t1.s = 0
            t1.ost = t1.ost - j
        elif t1.s == 0:
            playsound("budilnik.mp3")
