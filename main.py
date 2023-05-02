import pyshorteners
import pyperclip
import tkinter as tk
from tkinter import *


# create color
background_colour = '#000000'
f1 = '#FFEBCD'
f2 = '#ffffff'

# window
window = tk.Tk()
window.title("")
window.geometry('500x450')
window.configure(bg=background_colour)

# frames
# frame_line = tk.Frame(window, width=700, height=20, bg="light blue")
#frame_line.grid(row=0, column=0)
frame_body = tk.Frame(window, width=700, height=590, bg=f2)
frame_body.grid(row=1, column=0)

# frame body
otp_region = tk.Label(frame_body, text="Welcome To URL shortner", height=1, font=('Ivy 18 bold'), fg="light blue",
                      bg=f2)
otp_region.place(x=105, y=10)

## long URL region
input_URL_name = tk.Label(frame_body, text="Enter URL", height=1, font=('Ivy 15 bold'), fg="pink", bg=f2)
input_URL_name.place(x=185, y=55)
input_URL = tk.Entry(frame_body, width=30)
input_URL.pack()
input_URL.place(x=155, y=85)

## sent otp
enter_url = tk.Label(frame_body, text="URL After Shortening", height=1, font=('Ivy 15 bold'), fg="pink", bg=f2)
enter_url.place(x=150, y=160)
input_url = tk.Entry(frame_body, width=30)
input_url.pack()
input_url.place(x=155, y=190)

def shortenurl():
    url = input_URL.get()
    short_url = pyshorteners.Shortener().tinyurl.short(url)
    input_url.delete(0, END)
    input_url.insert(0, short_url)

##subit button
shorten_button = tk.Button(frame_body, text="Shorten", bd=2, font="arial 10", fg="black", bg="silver", height=1, command= shortenurl
                          )
shorten_button.place(x=210, y=130)

def copy():
    short_url = input_url.get()
    pyperclip.copy(short_url)



# copy button
check_button = tk.Button(frame_body, text="Copy URL", bd=1, font="arial 10", fg="black", bg="silver", height=1
                      ,command=copy)
check_button.place(x=195, y=240)
window.mainloop()