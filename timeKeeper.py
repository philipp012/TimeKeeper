import datetime
from ctypes import Structure, windll, c_uint, sizeof, byref
import time


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]


def get_idle_duration():
    last_input_info = LASTINPUTINFO()
    last_input_info.cbSize = sizeof(last_input_info)
    windll.user32.GetLastInputInfo(byref(last_input_info))
    millis = windll.kernel32.GetTickCount() - last_input_info.dwTime
    return millis / 1000.0


while 1:
    GetLastInputInfo = int(get_idle_duration())

    if GetLastInputInfo >= 10:
        startTime = datetime.datetime.now()
        start = time.time()

        while GetLastInputInfo >= 10:
            GetLastInputInfo = int(get_idle_duration())
            if GetLastInputInfo < 10:
                end = time.time()
                time_elapsed = end - start + 10

                duration = time.strftime('%H:%M:%S', time.gmtime(time_elapsed))
                if time_elapsed >= 10:
                    with open("C:\\Users\\M0231244\\Desktop\\timeKeeper.txt", 'w') as f:
                        f.write('From      ' + str(startTime.hour) + ':' + str(startTime.minute) +
                                '\nTo        ' + str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + '\nDuration  ' + str(duration))

