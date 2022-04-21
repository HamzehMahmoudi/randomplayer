import os 
import random 
directory = 'BASE_DIR' # e.g: "D:\Series\friends\"
seasons =[f.__fspath__() for f in os.scandir(directory) if f.is_dir()]
season  = random.choice(seasons)
episodes = [f.__fspath__() for f in os.scandir(season) if f.is_file()]
episode = random.choice(episodes)
path = os.path.abspath(episode)
command = '"{}"'.format(path)
os.system(command)
