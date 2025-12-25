Python Keylogger Overview

This project is a Python-based keystroke logging program developed to understand keyboard event handling, file logging, timestamps, and keyboard input processing. The application captures keyboard input, appends timestamps, and stores the data in a text file.

⚠️ Educational Use Only
This project is strictly for learning and experimentation on systems you own or have explicit permission to use.

Features

Captures keyboard keystrokes in real time

Logs data into mydata.txt

Adds timestamps for better tracking

Handles common keys:

Characters

Space, Enter, Tab

Backspace

Special keys (logged with readable labels)

File Structure
keylogger/
│
├── keystroke.py     # Python source code
└── mydata.txt       # Output log file

How It Works

The program listens for keyboard events using pynput

Each keystroke is processed and appended to an in-memory string

On every key press, the content is written to mydata.txt

Pressing Enter inserts a new line with a timestamp

Special keys are logged using readable labels for clarity

Execution

Run the program using Python:

python keystroke.py


Once executed, the program immediately begins logging keystrokes into mydata.txt.

Technologies Used

Python

pynput

datetime
