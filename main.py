import tkinter
import customtkinter
from pytube import YouTube

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# App frame/ window
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")


# Add UI Elements
title = customtkinter.CTkLabel(
    app, text="Insert a YouTube link", font=("Arial", 20))

title.pack(pady=10, padx=10)


# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack(pady=10, padx=10)



# Run app
app.mainloop()
