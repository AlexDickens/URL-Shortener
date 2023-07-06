import pyshorteners
from tkinter import * 
import tkinter as tk
import pyperclip
from win10toast import ToastNotifier
import ttkbootstrap as tk

def urlShorten():
    urls = pyshorteners.Shortener()
    url = entry.get()
    newURl = urls.tinyurl.short(url)
    pyperclip.copy(newURl)

    noti = ToastNotifier()
    noti.show_toast("Congrats", "Your shortened URL has been copied to clipboard")

    

root = tk.Window(themename = "journal")
root.geometry("240x100")
root.title = "URL Shortener"
entry = tk.Entry(root)
entry.pack(side = "left", padx = 10)
button = tk.Button(root, text = "Shorten", command = urlShorten)
button.pack(side = "left", padx = 10)



root.mainloop()

