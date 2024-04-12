import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import PhotoImage
import os

directory_path = 'C:/Program Files/Fayda/packets/packet-manager'

def on_submit():
    search_string_to_find = entry_name.get()
    result = search_string_in_files(directory_path, search_string_to_find)
    if result: 
        for file_name in result:
            file_path = os.path.join(directory_path, file_name)
            open_file_location(file_path)
    else:
        messagebox.showwarning("Searching has been complated", "No result!")      
     
def search_string_in_files(directory, search_string):
    matching_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if search_string !="" and search_string in content:
                        matching_files.append(file_path)
    return matching_files

def open_directory():
    global directory_path
    new_path = filedialog.askdirectory()
    if new_path:
        directory_path = new_path

def open_file_location(file):
    os.startfile(file)

root = tk.Tk()
root.title("ማሰሻ")
root.iconbitmap("fayda.ico")
root.geometry('1000x380')
root.resizable(False, False)
bg_image = PhotoImage(file="C:/search/bk.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

container1 = Frame(root)
container1.pack(side=BOTTOM)
 
label_name = tk.Label(container1, text="የተመዘገቡበትን ስልክ ቁጥር ወይም ሙሉ ስም ያስገቡ:", fg="#209099", font=("Nyala", 20), borderwidth=4)
label_name.grid(row=0, column=0, padx=20, pady=10, sticky="w")

entry_name = tk.Entry(container1, font=("Nyala", 20), borderwidth=4)
entry_name.grid(row=0, column=1, padx=30, pady=0)

open_button = tk.Button(container1, text="ምረጥ",font=("Nyala", 14), command=open_directory, background="#209099", fg="white")
open_button.grid(row=0, column=2, padx=20, pady=10)

def enter(event):
    submit_button['background'] = 'black'

def leave(event):
    submit_button['background'] = '#209099'
    
submit_button = tk.Button(container1, text="ፈልግ",font=("Nyala",14), command=on_submit,background="#209099", fg="white")
submit_button.grid(row=4, column=0, columnspan=2, pady=10)
submit_button.bind('<Enter>', enter)
submit_button.bind('<Leave>', leave)

root.mainloop()
