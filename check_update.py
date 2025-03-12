import time

import requests
import os
import sys
import subprocess
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk


CURRENT_VERSION = "4.0"  # Change with every new release
VERSION_URL = "https://a-g-auto-policy-push-software.vercel.app/A&GPushVersion.txt"  # URL to  the latest version
INSTALLER_URL = "https://github.com/ITACHI1117/A-G-update-exe/raw/refs/heads/main/A&G%20Policy%20Updater%20setup.exe"  # URL to the latest installer
INSTALLER_PATH = "update_installer.exe"  # Temporary installer filename


def check_for_update(root):
    # result_queue = False
    try:
        response = requests.get(VERSION_URL)
        latest_version = response.text.strip()  # Get the latest version from the site

        if latest_version != CURRENT_VERSION:
            # willUpdate = messagebox.askyesno("Software update","A new version ({latest_version}) is available!, Do you want to download the latest update?")
            messagebox.showinfo("Software update",
                                f"A new version ({latest_version}) is available! Download has started automatically, the installer will run when the downlaod is complete.")
            print(f"A new version ({latest_version}) is available! \n Click Ok to Update, the installer will run when the downlaod is complete.")
            download_update(root)
            root.destroy()
            os._exit(0)
            sys.exit()  # Fully terminate the program
            # if willUpdate:
            #     download_update()

            result_queue = True

        else:
            # messagebox.showinfo("Software Update","You are using the latest version")
            print("You are usingr the latest version.")
    except requests.RequestException:
        # messagebox.showinfo("Software Update", "Could not check for updates. Please ensure you are online.")
        print("Could not check for updates. Please ensure you are online.")


def download_update(root):
    progress_var = tk.IntVar(value=0)  # Tkinter variable for progress
    open_download_window(root, progress_var)
    try:
        print("Downloading the latest version...")
        response = requests.get(INSTALLER_URL, stream=True)
        total_size = int(response.headers.get("content-length", 0))  # Get file size

        downloaded_size = 0
        with open(INSTALLER_PATH, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
                    downloaded_size += len(chunk)

                    # Update Progress Bar
                    progress_percent = (downloaded_size / total_size) * 100
                    print(progress_percent)
                    progress_var.set(int(progress_percent))

                    # progress_bar["value"] = progress_percent
                    # root.update_idletasks()  # Refresh UI

        print("Download complete! Installing update...")
        install_update()
    except requests.RequestException:
        print("Update download failed. Please try again later.")


def install_update():
    print("Closing application and launching installer...")

    # Launch the installer and exit the current application
    subprocess.Popen([INSTALLER_PATH], shell=True)



def open_download_window(root, progress_var):
    """Creates a window with a progress bar"""
    download_window = tk.Toplevel(root)
    download_window.iconbitmap("./A&GICON.ico")
    download_window.title("Downloading Update")
    download_window.geometry("700x150")

    tk.Label(download_window, text="Downloading...").pack(pady=10)

    progress_bar = ttk.Progressbar(download_window,  orient="horizontal", length=250, variable=progress_var, bootstyle="success")
    progress_bar.pack(pady=10)


