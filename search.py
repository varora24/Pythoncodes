import pyautogui
import webbrowser
import random
import requests
import time

URL = "https://www.bing.com/"
words_url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

words = requests.get(words_url)
searches = words.text.splitlines()

for i in range(60):
    choose_word = random.randint(120,400000)

    webbrowser.open_new(URL)

    #print(searches[choose_word])
    time.sleep(random.randint(3,10))
    pyautogui.typewrite(searches[choose_word],interval=0.01)
    pyautogui.typewrite('\n',interval=0.1)
    pyautogui.hotkey('ctrl','w')
    numsearch = i+1

print(f'{numsearch} searches completed :)')
