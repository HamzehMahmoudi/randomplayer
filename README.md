# randomplayer
i watch a random episode of my favorite shows in my free time\
so i wrote simple script to play random episode for me :)\
you can `config.py` to change the list of shows and the path to your shows
```json
series = {
    "friends": 'PATH TO FRIENDS SEASONS',
    "office": 'PATH TO OFFICE SEASONS',
    "familyguy": 'PATH TO FAMILY GUY SEASONS',
    "himym": 'PATH TO HIMYM SEASONS',
}
```

## Requirement
 - python

## Usage
`python -m player.py show_name `
if you dont enter the show name it will play random show from the list in 'config.py'
