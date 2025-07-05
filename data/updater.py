import json, os, sys, requests, pathlib, minecraft_launcher_lib, shutil
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from pathlib import Path
from lang import lang, current_language
from variables import check_network
import variables

def version_to_tuple(version):
    if 'alpha' in version:
        version_type = 0
        version = version.replace('alpha-', '')
    elif 'beta' in version:
        version_type = 1
        version = version.replace('beta-', '')
    else:
        version_type = 2
    parts = version.split('.')
    return (version_type,) + tuple(map(int, parts))

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        super().__init__(parent, title)

    def body(self, master):
        tk.Label(master, text="Which format would you like to download?", font=("Arial", 12)).grid(row=0, pady=10)
        self.choice = tk.StringVar()
        self.choice.set("bin")
        tk.Radiobutton(master, text=".bin", variable=self.choice, value="bin", font=("Arial", 10)).grid(row=1, sticky=tk.W, padx=20)
        tk.Radiobutton(master, text=".deb", variable=self.choice, value="deb", font=("Arial", 10)).grid(row=2, sticky=tk.W, padx=20)
        return None

    def apply(self):
        self.result = self.choice.get()

def download_file(url, dest, progress_var, progress_bar, progress_label):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0)) or 1
    block_size = 1024
    downloaded_size = 0
    
    if os.path.exists(dest):
        # if the file already exists, check if the file is the same size as the one being downloaded
        if os.path.getsize(dest) == total_size:
            return True
        else:
            os.remove(dest)

    with open(dest, 'wb') as file:
        for data in response.iter_content(block_size):
            file.write(data)
            downloaded_size += len(data)
            progress_var.set((downloaded_size / total_size) * 100)
            progress_bar['value'] = (downloaded_size / total_size) * 100
            progress_label.config(text=f"{int((downloaded_size / total_size) * 100)}%")
            progress_bar.update_idletasks()

    if total_size != 0 and downloaded_size != total_size:
        show_custom_message("Error", "Something went wrong during the download.", "error")
        return False
    return True

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def show_custom_message(title, message, msg_type="info"):
    custom_window = tk.Toplevel()
    custom_window.title(title)
    custom_window.iconphoto(False, tk.PhotoImage(file=variables.icon))
    tk.Label(custom_window, text=message, padx=20, pady=20, font=("Arial", 12)).pack()
    tk.Button(custom_window, text="OK", command=custom_window.destroy, width=15, font=("Arial", 10)).pack(pady=10)
    center_window(custom_window)
    custom_window.transient()
    custom_window.grab_set()
    custom_window.wait_window()

def clean_up():
    try:
        os.remove(os.path.join(variables.app_directory, "updates", "update.exe"))
    except:
        pass
    try:
        os.remove(os.path.join(variables.app_directory, "updates", "update.bin"))
    except:
        pass
    try:
        os.remove(os.path.join(variables.app_directory, "updates", "update.deb"))
    except:
        pass
    try:
        os.rmdir(os.path.join(variables.app_directory, "updates"))
    except:
        pass

def update():
    pass
if __name__ == "__main__":
    update()