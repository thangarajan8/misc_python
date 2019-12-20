from pynput.keyboard import Listener
from datetime import datetime

def on_press(key):
    print('{0},{1}'.format(key,str(datetime.now())))

# Collect events until released
with Listener(
        on_press=on_press
        ) as listener:
    listener.join()