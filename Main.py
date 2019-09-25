import requests
from time import sleep

uuid = input('Enter your R6 Tab UUID:')
start = input('Type "Start" to begin sending:')
sentBots = 0
if start != 'Start':
    print('Invalid Line. Quitting.')
    sleep(2.0)
    exit()
else:
    while True:
        WebRequest = requests.get('https://r6tab.com/mainpage.php?page='+uuid)
        sentBots = sentBots + 1
        print(f'[{sentBots}]: Bot Sent Successfully')
        
        
