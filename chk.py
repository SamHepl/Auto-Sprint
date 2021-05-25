from pynput.keyboard import Key, Listener, Controller

count = 0
keys = []

keyboard = Controller()

def on_press(key):
   global keys, count

   keys.append(key)
   count += 1

   if "{0}".format(key) == "'w'":
      keyboard.press(Key.ctrl)
      print('w found')

with Listener (on_press=on_press) as Listener:
   Listener.join()

ww