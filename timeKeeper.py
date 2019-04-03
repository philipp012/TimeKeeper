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


while True:
    GetLastInputInfo = int(get_idle_duration())
    startTime = datetime.datetime.now()
    start = time.time()
    while GetLastInputInfo >= 600:
        GetLastInputInfo = int(get_idle_duration())
        if GetLastInputInfo < 600:
            end = time.time()
            time_elapsed = end - start

            duration = time.strftime('%H:%M:%S', time.gmtime(time_elapsed))
            if time_elapsed >= 10:
                with open("H:\\timeKeeper.txt", 'w') as f:
                    f.write('Date: ' + datetime.datetime.today().strftime('%Y-%m-%d') + '\nFrom      ' + str(
                        startTime.hour) + ':' + str(startTime.minute) +
                            '\nTo        ' + str(datetime.datetime.now().hour) + ':' +
                            str(datetime.datetime.now().minute) + '\nDuration  ' + str(duration))
        time.sleep(5)
    time.sleep(5)
