import datetime
from ctypes import Structure, windll, c_uint, sizeof, byref
import time


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


while 1:
    GetLastInputInfo = int(get_idle_duration())

    if GetLastInputInfo >= 10:
        start = time.time()
        startTime = time.strftime('%H:%M', time.gmtime(start + 1))

        while GetLastInputInfo >= 10:
            GetLastInputInfo = int(get_idle_duration())
            if GetLastInputInfo < 10:
                end = time.time()
                time_elapsed = end - start + 10

                duration = time.strftime('%H:%M:%S', time.gmtime(time_elapsed))
                if time_elapsed >= 10:
                    with open("H:\\timeKeeper.txt", 'w') as f:
                        f.write('Date      ' + str(datetime.datetime.now().weekday()) + '.' + str(
                            datetime.datetime.now().month) + '.' + str(
                            datetime.datetime.now().year) + '\nFrom      ' + str(
                            datetime.datetime.now().hour) + ':' + str(
                            datetime.datetime.now().minute) + '\nTo        ' + str(
                            datetime.datetime.now().hour) + ':' + str(
                            datetime.datetime.now().minute) + '\nDuration  ' + str(duration))
