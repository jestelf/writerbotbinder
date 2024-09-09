from pynput import keyboard as pynput_keyboard
import keyboard as kbd
import time

def custom_typing(message, delay=0.06):  # delay=0.1 задает задержку в 0.1 секунду между символами
    for char in message:
        kbd.write(char)
        time.sleep(delay)

def on_activate_f1():
    code = """

    """
    custom_typing(code)

shift_pressed = False
def on_press(key):
    global shift_pressed
    if key == pynput_keyboard.Key.shift:
        shift_pressed = True

def on_release(key):
    global shift_pressed
    if key == pynput_keyboard.Key.shift:
        shift_pressed = False
    elif shift_pressed:  # Если Shift зажат
        if key == pynput_keyboard.Key.f1:
            on_activate_f1()
    if key == pynput_keyboard.Key.delete:  # Если нажата клавиша Del
        listener.stop()  # Останавливаем слушателя

with pynput_keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
