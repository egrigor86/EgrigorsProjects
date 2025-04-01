This repository is a personal collection of small, useful programs I’ve created to improve my workflow, save time, and eliminate repetitive tasks. Each tool in here is built with simplicity, speed, and real-world use in mind. If you find them useful too — awesome. If not, well, they make my life easier.

This is my stash of "why hasn't anyone made this already?" scripts.

Included Tools (so far)

🔹 Python Venv Creator GUI A lightweight tkinter GUI for quickly creating virtual environments from detected Python installs. Features:

Scans only C:/ root-level folders (like C:/Python310) for python.exe.

Lets you choose which Python interpreter to use.

Allows you to pick a folder to install the venv directly into — no subfolders.

Automatically creates a start.bat file in that folder to activate the environment instantly via Command Prompt.

Perfect for spinning up new isolated workspaces in seconds.


🔹 _launcher is a lightweight, cross-platform Python script launcher built with tkinter. It helps you run your local Python files quickly and easily — with version control, descriptions, and auto-detection of interpreters.

Features:
Auto-detects Python versions (Windows/Linux paths included)

Remembers custom Python paths between sessions

Reads script descriptions from the first line if it starts with ##

Detects script type: Streamlit, Python, or Unknown

One-click launch of scripts via your selected Python version

No dependencies — just pure Python + tkinter

Ideal For:
Developers juggling multiple Python environments

Streamlit app testers

Anyone who wants to stop typing commands in the terminal
