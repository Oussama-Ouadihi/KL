Keylogger Project
This project is a simple keylogger designed for educational purposes. It demonstrates how keylogging can work in Python using the pynput library. It includes two main files:

target.py: The keylogger client that captures keystrokes.
listener.py: The server that listens for and logs keystrokes sent from the client.
keylog.txt: The file where logged keystrokes are stored.
Requirements
To run this project, you need to have Python installed on both the server and the client machine. You can download Python from here.

Additionally, the project requires the following Python package:

pynput (for capturing keystrokes)
You can install the required package by running:

bash
Copy
Edit
pip install pynput
File Overview
target.py (Client)

Captures keystrokes from the keyboard.
Sends the captured keystrokes to the server (listener.py).
listener.py (Server)

Listens for incoming connections from the client.
Logs the keystrokes received in keylog.txt.
keylog.txt (Log File)

Stores the captured keystrokes with timestamps.
How to Run
On the Server (listener.py)
Ensure that the listener.py file is on the machine you want to use as the server.

Modify the HOST and PORT variables in listener.py to suit your testing or deployment configuration (default: HOST = "0.0.0.0" and PORT = 8080).

Note: For testing both scripts on a single device, the HOST value has been changed to "127.0.0.1" (localhost), allowing the client and server to communicate on the same device without needing an external network.

Run the server script:

bash
Copy
Edit
python listener.py
The server will start listening for incoming connections and log any keystrokes it receives in keylog.txt.

On the Client (target.py)
Ensure that the target.py file is on the machine you want to use as the client.
Modify the HOST and PORT variables in target.py to match the server configuration. If you're testing both scripts on the same device, make sure HOST = "127.0.0.1" and PORT matches the one in listener.py.
Run the client script:
bash
Copy
Edit
python target.py
The client will start capturing keystrokes and send them to the server.

Testing Both on the Same Machine
To test both scripts on the same device (i.e., both the server and client running on the same computer):

Run listener.py first (on the server machine).
Then run target.py (on the client machine) on the same machine, ensuring that both the HOST and PORT are set correctly to allow communication.
Deployment
In a real-life scenario, you may need to deploy the client (target.py) and server (listener.py) on separate devices. To remotely install and deploy the scripts, you can use methods like:

Remote Installation Script: Write a script that remotely installs the required Python environment and dependencies (like pynput) on the target device. This can be done through tools like Ansible or Fabric for automated remote management.

SSH Remote Control: Use SSH to remotely access and deploy the keylogger code to the target device. After logging in, you can copy over the Python scripts and execute them from the terminal.

For discreet deployment in a real-life scenario, you might also want to package your Python scripts into standalone executables using PyInstaller. This allows the client (target.exe) and listener (listener.exe) to run without requiring a Python installation.

To convert your Python scripts into executables, you can use:

PyInstaller (for packaging the code):

bash
Copy
Edit
pyinstaller --onefile --windowed target.py
pyinstaller --onefile --windowed listener.py
After packaging, you can distribute the executables to remote devices where you want to deploy the client (target.exe) and listener (listener.exe). Ensure that the executables are set to connect to the correct server.

Important Notes
Ethical Use Only: This project is intended for educational purposes only. Do not use this code to invade others' privacy or engage in unauthorized activities. Always obtain explicit consent before using such software in real-world scenarios.

Firewall and Port Configuration: The server listens on a specified port. If you're deploying this in a real-world scenario, ensure that firewalls and routers are properly configured to allow traffic on the desired port. Common ports like 80 or 443 are often unblocked for communication.

Disclaimer
This project is for educational purposes only. Any use of this code outside of a controlled environment where explicit consent is obtained may violate privacy and legal guidelines. Always respect the privacy of others and comply with local laws regarding computer usage.
