import os 
import random 
import potplayer as player
directory = 'BASE PATH' # e.g: "D:\Series\FRIENDS"
seasons =[f.name for f in os.scandir(directory) if f.is_dir()]
season  = random.choice(seasons)
episodes = [f.__fspath__() for f in os.scandir(season) if f.is_file() and f.name.endswith('.mkv')]
episode = random.choice(episodes)
path = os.path.abspath(episode)
player.run(path=path)
