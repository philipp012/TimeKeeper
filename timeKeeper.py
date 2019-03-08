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
        startTime = datetime.datetime.now()

        while GetLastInputInfo >= 10:
            GetLastInputInfo = int(get_idle_duration())
            if GetLastInputInfo < 10:
                end = time.time()
                time_elapsed = end - start + 10
                if time_elapsed >= 10:
                    with open("C:\\Users\\M0231244\\Desktop\\time.txt", 'w') as f:
                        f.write('Pause from ' + str(startTime) + ' to ' + str(
                            datetime.datetime.now()) + '\nDuration: ' + str(time_elapsed))
