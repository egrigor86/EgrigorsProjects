import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import subprocess

def find_python_versions():
    python_paths = []
    root_dirs = [os.path.join("C:/", d) for d in os.listdir("C:/") if os.path.isdir(os.path.join("C:/", d))]

    for dir_path in root_dirs:
        possible_path = os.path.join(dir_path, "python.exe")
        if os.path.exists(possible_path):
            python_paths.append(possible_path)
    
    return python_paths

def select_target_folder():
    folder = filedialog.askdirectory()
    if folder:
        target_folder.set(folder)

def create_virtual_env():
    python_path = selected_python.get()
    folder = target_folder.get()

    if not python_path or not folder:
        messagebox.showerror("Error", "Please select both Python version and target folder.")
        return

    try:
        subprocess.run([python_path, "-m", "venv", folder], check=True)
        bat_path = os.path.join(folder, "start.bat")
        activate_path = os.path.join(folder, "Scripts", "activate")
        with open(bat_path, "w") as f:
            f.write(f'start cmd /k "{activate_path}"')
        messagebox.showinfo("Success", f"Virtual environment created and start.bat generated at:\n{bat_path}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Failed to create virtual environment.\n{e}")

def start_search():
    python_listbox['values'] = ["Searching..."]
    root.after(100, update_python_versions)

def update_python_versions():
    python_paths = find_python_versions()
    if not python_paths:
        python_paths = ["No Python versions found."]
    python_listbox['values'] = python_paths
    selected_python.set(python_paths[0] if python_paths else "")

# GUI Setup
root = tk.Tk()
root.title("Python Venv Creator")

frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

selected_python = tk.StringVar()
target_folder = tk.StringVar()

ttk.Label(frame, text="1. Find Python Versions (like C:/Python310):").pack(anchor="w")
search_button = ttk.Button(frame, text="Search Python Installations", command=start_search)
search_button.pack(fill="x")

ttk.Label(frame, text="2. Select Python Version:").pack(anchor="w", pady=(10, 0))
python_listbox = ttk.Combobox(frame, textvariable=selected_python, state="readonly", width=80)
python_listbox.pack(fill="x")

ttk.Label(frame, text="3. Choose Folder to Install Virtual Env (no subfolder):").pack(anchor="w", pady=(10, 0))
ttk.Entry(frame, textvariable=target_folder, width=80).pack(fill="x")
ttk.Button(frame, text="Browse...", command=select_target_folder).pack()

ttk.Button(frame, text="4. Create Virtual Environment", command=create_virtual_env).pack(pady=(20, 0), fill="x")

root.mainloop()
