import tkinter as tk
import keyboard
import pyautogui as pag
import mouse

window = tk.Tk()
window.title("Rocket League Spammer")
window.configure(width=300, height=100)
window.configure(bg="white")

# keyboard set up
linkedKey = None
chatKey1 = None
chatKey2 = None

step = 0


def get_next_key():
    """get the next key pressed by keyboard, used to make key bind selections"""
    if keyboard.is_pressed('w'):
        return 'w'
    elif keyboard.is_pressed('a'):
        return 'a'
    elif keyboard.is_pressed('s'):
        return 's'
    elif keyboard.is_pressed('d'):
        return 'd'
    elif keyboard.is_pressed('left'):
        return 'left'
    elif keyboard.is_pressed('right'):
        return 'right'
    elif keyboard.is_pressed('up'):
        return 'up'
    elif keyboard.is_pressed('down'):
        return 'down'
    elif keyboard.is_pressed('space'):
        return 'space'
    elif keyboard.is_pressed('1'):
        return '1'
    elif keyboard.is_pressed('2'):
        return '2'
    elif keyboard.is_pressed('3'):
        return '3'
    elif keyboard.is_pressed('4'):
        return '4'
    elif keyboard.is_pressed('tab'):
        return 'tab'
    elif mouse.is_pressed('left'):
        return 'left mouse'
    elif mouse.is_pressed('right'):
        return 'right mouse'


def change_window():
    """change the tkinter window item, including prompt and button. uses steps
    variable to keep track of what step ofthe process the user is at"""
    global step

    if step == 0:
        strPrompt.set("Rocket League Spammer will ask you for a key to bind you spam to (Ex. WASD, boost, etc), "
                      "and the 1st and 2nd key correspond to the quick chat you would like to spam")
        btnText.set("Next")
        func.set("prompt1")
        step = 1
        return

    elif step == 1:
        strPrompt.set("Begin by pressing the button followed by the key you'd like to bind")
        btnText.set("BIND")
        step = 2
        return

    elif step == 2:
        button["state"] = "disabled"
        global linkedKey
        while not linkedKey:
            linkedKey = get_next_key()
        button["state"] = "normal"
        strPrompt.set("Got it! You selected \'" + linkedKey.upper() + "\' as your key")
        btnText.set("Next")
        step = 3
        return

    elif step == 3:
        strPrompt.set("Now press the button followed by the FIRST key of the quick chat you are binding")
        btnText.set("BIND KEY 1")
        step = 4
        return

    elif step == 4:
        button["state"] = "disabled"
        global chatKey1
        while not chatKey1:
            chatKey1 = get_next_key()
        button["state"] = "normal"
        strPrompt.set("Got it! You selected \'" + chatKey1.upper() + "\' as the first quick chat key")
        btnText.set("Next")
        step = 5
        return

    elif step == 5:
        strPrompt.set("Now press the button followed by the SECOND key of the quick chat you are binding")
        btnText.set("BIND KEY 2")
        step = 6
        return

    elif step == 6:
        button["state"] = "disabled"
        global chatKey2
        while not chatKey2:
            chatKey2 = get_next_key()
        button["state"] = "normal"
        strPrompt.set("Got it! You selected \'" + chatKey2.upper() + "\' as the second quick chat key")
        btnText.set("Next")
        step = 7
        return

    elif step == 7:
        strPrompt.set("You have selected \'" + linkedKey.upper() + "\' as you bind, and \'" + chatKey1 + " " + chatKey2 + "\' as your quick chat")
        step = 8
        return

    elif step == 8:
        strPrompt.set("All set! Press ` anytime to exit the program. Press the button to begin")
        btnText.set("BEGIN")
        step = 9
        return

    elif step == 9:
        window.destroy()
        exitLoop = False
        while not exitLoop:

            if linkedKey == "left mouse" or linkedKey == "right mouse":
                linkedKey = linkedKey[:-6]
                if mouse.is_pressed(linkedKey):
                    pag.press(chatKey1)
                    pag.press(chatKey2)
                linkedKey = linkedKey + " mouse"
            else:
                if keyboard.is_pressed(linkedKey):
                    pag.press(chatKey1)
                    pag.press(chatKey2)

            if keyboard.is_pressed('`'):
                exitLoop = True
    else:
        strPrompt.set("Something went wrong...")
        return


strPrompt = tk.StringVar()
btnText = tk.StringVar()
func = tk.StringVar()
strPrompt.set("Welcome to Rocket League Spammer!")
btnText.set("Begin")
func.set("prompt0")

prompt = tk.Label(window, textvariable=strPrompt)
button = tk.Button(textvariable=btnText, command=change_window)
button.pack()
prompt.pack()

window.mainloop()
