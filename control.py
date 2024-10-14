
from pynput.mouse import Controller
from pynput.keyboard import Controller


def controlmouse():
    mouse = Controller()
    mouse.position = (1000 , 2000)

def controlkeyboard():
    keyboard = Controller()
    keyboard.type("i am freaking awesome!")


controlkeyboard()