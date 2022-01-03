import tkinter as tk
import Ctkinter as Ctk
import get_music_lib as lib


root = tk.Tk()
root.geometry("800x500")

wid = lib.Get_music(root)
wid.get_music_window.place(x=0, y=0)



root.mainloop()
