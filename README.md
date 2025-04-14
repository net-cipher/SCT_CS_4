## Linux Keylogger (Educational Only)

> ⚠️ DISCLAIMER: This tool is developed for **educational purposes only**. Do **not** use this software on devices you do not own or without explicit permission. Unauthorized use may violate privacy laws and is considered illegal.

---

## Description

A simple keylogger built using Python and `pynput` to capture keystrokes on Linux systems. This project is intended for educational use, ethical hacking, and cybersecurity learning labs.

---

## Features

- Records all typed keystrokes
- Works in the background
- Simple and lightweight
- Saves logs to a local file

---

## 🐧 Installation (Kali Linux / Ubuntu / Debian)

### 1. Clone this repo
```bashgit clone https://github.com/net-cipher/SCT_CS_4.git```

### Change directory
```cd keylogger```

### Update Your Machine 
```sudo apt update```

### Install PIP and python3
```sudo apt install python3 python3-pip -y```

### Install pynput for keyboard library package
```pip3 install pynput```

### Run the program
```python3 keylogger.py```

After clicking CTRL + C , the keylogger will stop and after typing "ls" in the terminal, There will be an "keylog.txt" file,
use this command to view the keystrokes captured by the keylogger.
```cat keylog.txt```

Please use this tool with legal authrozied only. Do not use it for illegal purpose, i dont claim for it! Thank You
