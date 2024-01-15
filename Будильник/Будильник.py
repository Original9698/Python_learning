import vlc
from datetime import *
import os
import time
from mutagen.mp3 import MP3

# os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
time_treck = MP3('Знаешь ли ты.mp3')

alarm_time = {'hour': int(input()), 'min': int(input())}


def validate_time(time):
    if time['hour'] > 23 and time['hour'] < 0:
        return 'Неверный формат времени'
    elif time['min'] > 59 and time['min'] < 0:
        return 'Неверный формат времени'
    else:
        return 'Время установлено'


print(validate_time(alarm_time))

media = vlc.MediaPlayer('D:\Alarm\Знаешь ли ты.mp3')

while True:
    now = datetime.now()

    if now.hour == alarm_time['hour'] and now.minute == alarm_time['min']:
        media.play()
        print("Пора вставать!")
        time.sleep(time_treck.info.length)
        break

    time.sleep(60)
