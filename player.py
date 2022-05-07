import os 
import random
from config import series 
import sys
print(sys.argv)
try:
    directory = series[sys.argv[1]]
except IndexError:
    show = random.choice(list(series.keys()))
    directory = series[show] 
finally:
    seasons =[f.__fspath__() for f in os.scandir(directory) if f.is_dir()]
    season  = random.choice(seasons)
    episodes = [f.__fspath__() for f in os.scandir(season) if f.is_file() and (f.name.endswith('.mkv') or f.name.endswith('.mp4') or f.name.endswith('.avi'))]
    episode = random.choice(episodes)
    path = os.path.abspath(episode)
    print(f"Playing {episode}")
    sysname = os.name
    if sysname == "posix":
        command = f"open {path}"
    else:
        command = '"{}"'.format(path)
    os.system(command)
