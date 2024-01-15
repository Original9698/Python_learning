import os

path = 'C:\Program Files\VideoLAN\VLC'

print(os.listdir(path))
for i in os.listdir(path):
    print(i, path + '\\' + i)