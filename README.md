Python Keylogger (.exe)
Overview

This project is a Python-based keystroke logging program developed to understand keyboard event handling, file logging, timestamps, and executable deployment. The application captures keyboard input, appends timestamps, and stores the data in a text file. The Python script was converted into a Windows .exe for standalone execution.

⚠️ Educational Use Only
This project is strictly for learning and experimentation on systems you own or have permission to use.

Features

Captures keyboard keystrokes in real time

Logs data into mydata.txt

Adds timestamps for better tracking

Handles common keys:

Characters

Space, Enter, Tab

Backspace

Special keys (logged with labels)

Runs as a standalone .exe (no Python required)

File Structure
keylogger/
│
├── build/                # Build files generated during exe creation
├── dist/
│   ├── keystroke.exe     # Executable file
│   └── mydata.txt        # Output log file
│
├── keystroke.py          # Original Python source code
├── keystroke.spec        # PyInstaller spec file
└── mydata.txt            # Log file (used during testing)

How It Works

The program listens for keyboard events using pynput

Each keystroke is processed and appended to an in-memory string

On every key press, the content is written to mydata.txt

Pressing Enter inserts a new line with a timestamp

Special keys are logged with readable labels

Execution

You can run the program in two ways:

1. Using Python
   
python keystroke.py

2. Using Executable
   
dist/keystroke.exe


Running the .exe will automatically start logging keystrokes into mydata.txt.

Technologies Used

Python

pynput

datetime

PyInstaller (for .exe conversion)
