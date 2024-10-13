import time
import keyboard
import mouse
import pyautogui

screen_width, screen_height = pyautogui.size()

center_x = screen_width // 2
center_y = screen_height // 2

SENSITIVITY = 10  

pyautogui.FAILSAFE = False

holding_keys = {'up': False, 'down': False, 'left': False, 'right': False}

def press_key(key_name, key_value):
    if not holding_keys[key_name]:
        keyboard.press(key_value)
        holding_keys[key_name] = True
        print(f"{key_value} key pressed")

def release_key(key_name, key_value):
    if holding_keys[key_name]:
        keyboard.release(key_value)
        holding_keys[key_name] = False
        print(f"{key_value} key released")

def on_move():
    while True:  
        x, y = mouse.get_position()
  
        dx = x - center_x
        dy = y - center_y
        
        if dy < -SENSITIVITY:  
            press_key('up', 'i')
            release_key('down', 'k')
        elif dy > SENSITIVITY:  
            press_key('down', 'k')
            release_key('up', 'i')
        else:  
            release_key('up', 'i')
            release_key('down', 'k')

        if dx < -SENSITIVITY:  
            press_key('left', 'j')
            release_key('right', 'l')
        elif dx > SENSITIVITY:  
            press_key('right', 'l')
            release_key('left', 'j')
        else:  
            release_key('left', 'j')
            release_key('right', 'l')
        
        pyautogui.moveTo(center_x, center_y)
       
        time.sleep(0.01)

pyautogui.moveTo(center_x, center_y)

try:
    on_move()
except KeyboardInterrupt:
    print("Program exited")
