import tkinter as tk
import keyboard as kb
import pyautogui as pag
import mouse as ms
from pynput import keyboard, mouse
from time import sleep, time

window = tk.Tk()
window.title("Rocket League Spammer")
window.configure(width=300, height=100)
window.configure(bg="white")

# keyboard set up
linkedKey = None
chatKey1 = None
chatKey2 = None

step = 0
accepting = True


def get_next_key():
    """get the next key pressed by keyboard, used to make key bind selections"""
    if kb.is_pressed('w'):
        return 'w'
    elif kb.is_pressed('a'):
        return 'a'
    elif kb.is_pressed('s'):
        return 's'
    elif kb.is_pressed('d'):
        return 'd'
    elif kb.is_pressed('left'):
        return 'left'
    elif kb.is_pressed('right'):
        return 'right'
    elif kb.is_pressed('up'):
        return 'up'
    elif kb.is_pressed('down'):
        return 'down'
    elif kb.is_pressed('space'):
        return 'space'
    elif kb.is_pressed('1'):
        return '1'
    elif kb.is_pressed('2'):
        return '2'
    elif kb.is_pressed('3'):
        return '3'
    elif kb.is_pressed('4'):
        return '4'
    elif kb.is_pressed('tab'):
        return 'tab'
    # elif ms.is_pressed('left'):
    #     return 'left mouse'
    # elif ms.is_pressed('right'):
    #     return 'right mouse'


def change_window():
    """change the tkinter window item, including prompt and button. uses steps
    variable to keep track of what step of the process the user is at"""
    global step

    if step == 0:
        strPrompt.set("Rocket League Spammer will ask you for a key to bind you spam to (Ex. WASD, boost, etc), "
                      "and the 1st and 2nd key correspond to the quick chat you would like to spam")
        btnText.set("Next")
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
        global exitLoop
        exitLoop = False
        while not exitLoop:
            with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
                print("listening")
                listener.join()

            # if linkedKey == "left mouse" or linkedKey == "right mouse":
            #     linkedKey = linkedKey[:-6]
            #     with mouse.Listener(on_press=on_press) as listener:
            #         listener.join()
            #     linkedKey = linkedKey + " mouse"
            # else:
    else:
        strPrompt.set("Something went wrong...")
        return


def on_release(key):
    global accepting
    if not accepting:
        if key == keyboard.Key.space:
            accepting = True
        elif key == keyboard.Key.tab:
            accepting = True
        elif key == keyboard.Key.up:
            accepting = True
        elif key == keyboard.Key.down:
            accepting = True
        elif key == keyboard.Key.left:
            accepting = True
        elif key == keyboard.Key.right:
            accepting = True
        elif key == keyboard.Key.up:
            print("up :|")
        elif key == keyboard.Key.down:
            print("down :|")
        elif key == keyboard.Key.left:
            print("left :|")
        elif key == keyboard.Key.right:
            print("right :|")
        elif key == keyboard.Key.space:
            print("space :|")
        elif key == keyboard.Key.esc:
            print("esc :|")
        elif key == keyboard.Key.ctrl_l:
            print("ctrl :|")
        elif key == keyboard.Key.ctrl_r:
            print("ctrl :|")
        elif key == keyboard.Key.shift_l:
            print("shift_l :|")
        elif key == keyboard.Key.shift_r:
            print("shift_r :|")
        elif key == keyboard.Key.backspace:
            print("backspace :|")
        elif key == keyboard.Key.alt_l:
            print("alt_l :|")
        elif key == keyboard.Key.caps_lock:
            print("caps_lock :|")
        elif key == keyboard.Key.cmd_l:
            print("cmd_l :|")
        elif key == keyboard.Key.cmd_r:
            print("cmd_r :|")
        elif key == keyboard.Key.delete:
            print("delete :|")
        elif key == keyboard.Key.enter:
            print("enter :|")
        elif key == keyboard.Key.media_next:
            print("media_next :|")
        elif key == keyboard.Key.media_play_pause:
            print("media_play_pause :|")
        elif key == keyboard.Key.tab:
            print("tab :|")
        elif (key.char == 'w') \
                or (key.char == 'a') \
                or (key.char == 's') \
                or (key.char == 'd'):
            accepting = True


def on_press(key):
    global accepting
    if accepting:
        print("pressed and used")
    else:
        print("")
    if accepting:
        accepting = False
        if 'space' == linkedKey and key == keyboard.Key.space:
            pag.press(chatKey1)
            pag.press(chatKey2)
        elif 'tab' == linkedKey and key == keyboard.Key.tab:
            pag.press(chatKey1)
            pag.press(chatKey2)
        elif 'up' == linkedKey and key == keyboard.Key.up:
            pag.press(chatKey1)
            pag.press(chatKey2)
        elif 'down' == linkedKey and key == keyboard.Key.down:
            pag.press(chatKey1)
            pag.press(chatKey2)
        elif 'left' == linkedKey and key == keyboard.Key.left:
            pag.press(chatKey1)
            pag.press(chatKey2)
        elif 'right' == linkedKey and key == keyboard.Key.right:
            pag.press(chatKey1)
            pag.press(chatKey2)
        elif key == keyboard.Key.up:
            print("up :|")
        elif key == keyboard.Key.down:
            print("down :|")
        elif key == keyboard.Key.left:
            print("left :|")
        elif key == keyboard.Key.right:
            print("right :|")
        elif key == keyboard.Key.space:
            print("space :|")
        elif key == keyboard.Key.esc:
            print("esc :|")
        elif key == keyboard.Key.ctrl_l:
            print("ctrl :|")
        elif key == keyboard.Key.ctrl_r:
            print("ctrl :|")
        elif key == keyboard.Key.shift_l:
            print("shift_l :|")
        elif key == keyboard.Key.shift_r:
            print("shift_r :|")
        elif key == keyboard.Key.backspace:
            print("backspace :|")
        elif key == keyboard.Key.alt_l:
            print("alt_l :|")
        elif key == keyboard.Key.caps_lock:
            print("caps_lock :|")
        elif key == keyboard.Key.cmd_l:
            print("cmd_l :|")
        elif key == keyboard.Key.cmd_r:
            print("cmd_r :|")
        elif key == keyboard.Key.delete:
            print("delete :|")
        elif key == keyboard.Key.enter:
            print("enter :|")
        elif key == keyboard.Key.media_next:
            print("media_next :|")
        elif key == keyboard.Key.media_play_pause:
            print("media_play_pause :|")
        elif key == keyboard.Key.tab:
            print("tab :|")
        elif ('w' == linkedKey and key.char == 'w') \
                or ('a' == linkedKey and key.char == 'a') \
                or ('s' == linkedKey and key.char == 's') \
                or ('d' == linkedKey and key.char == 'd'):
            pag.press(chatKey1)
            pag.press(chatKey2)
        elif key.char == '`':
            print("Exit")
            global exitLoop
            exitLoop = True
            exit(0)


strPrompt = tk.StringVar()
btnText = tk.StringVar()
strPrompt.set("Welcome to Rocket League Spammer!")
btnText.set("Begin")

prompt = tk.Label(window, textvariable=strPrompt)
button = tk.Button(textvariable=btnText, command=change_window)
button.pack()
prompt.pack()

window.mainloop()
