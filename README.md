# Keylogger Project

> ⚠️ **Disclaimer**: This project is for educational purposes only. Any use of this code outside of a controlled environment where explicit consent is obtained may violate privacy and legal guidelines. Always respect the privacy of others and comply with local laws regarding computer usage.

## Overview

This project is a simple keylogger designed for educational purposes. It demonstrates how keylogging can work in Python using the `pynput` library. 

### Components

* `target.py` - The keylogger client that captures keystrokes
* `listener.py` - The server that listens for and logs keystrokes sent from the client
* `keylog.txt` - The file where logged keystrokes are stored

## Prerequisites

* Python installed on both server and client machines ([Download Python](https://www.python.org/downloads/))
* Required Python package:
  ```bash
  pip install pynput
  ```

## File Structure

### target.py (Client)
* Captures keystrokes from the keyboard
* Sends the captured keystrokes to the server

### listener.py (Server)
* Listens for incoming connections from the client
* Logs the keystrokes received in keylog.txt

### keylog.txt
* Stores the captured keystrokes with timestamps

## Setup and Usage

### Server Setup (listener.py)

1. Place `listener.py` on the machine you want to use as the server
2. Configure the HOST and PORT variables:
   * Default: `HOST = "0.0.0.0"`, `PORT = 8080`
   * For local testing: `HOST = "127.0.0.1"`
3. Run the server:
   ```bash
   python listener.py
   ```

### Client Setup (target.py)

1. Place `target.py` on the target machine
2. Ensure HOST and PORT match server configuration
3. Run the client:
   ```bash
   python target.py
   ```

## Testing Locally

To test both components on the same machine:

1. Start `listener.py` first
2. Run `target.py` second
3. Ensure both use `HOST = "127.0.0.1"` and matching PORT values

## Deployment Guide

### Remote Deployment Options

1. **Remote Installation Script**
   * Use tools like Ansible or Fabric for automated deployment
   * Install Python environment and dependencies remotely

2. **SSH Remote Control**
   * Deploy via SSH access
   * Copy and execute scripts through terminal

### Creating Standalone Executables

Use PyInstaller to create standalone executables:

```bash
pyinstaller --onefile --windowed target.py
pyinstaller --onefile --windowed listener.py
```

This creates:
* `target.exe` - Deployable client executable
* `listener.exe` - Deployable server executable

## Important Considerations

### Security and Network Configuration

* Ensure proper firewall configuration for chosen ports
* Common ports (80, 443) are typically unblocked
* Configure router settings if needed for external access

### Ethical Guidelines

* Obtain explicit consent before deployment
* Use only in controlled, authorized environments
* Respect privacy and data protection laws
* Document all deployments and usage

## Technical Notes

* Remote deployment requires proper Python environment setup
* Consider network security implications
* Test thoroughly in controlled environment first
* Monitor system resource usage
* Implement proper error handling and logging
