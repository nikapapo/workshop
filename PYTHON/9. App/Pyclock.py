# IMPORTS
#================

import tkinter
import time


# WINDOW
#===========================
# create the window
win = tkinter.Tk()#amit ickeba

win.title("A simple clock with Python Tkinter")
screen_width = win.winfo_screenwidth() #centrireba
screen_height =win.winfo_screenheight() #centrireba


win_pos_x = int((screen_width / 2) - 250)
win_pos_y = int ((screen_height / 2) - 150 -55 )


win.geometry(f"500x300+{win_pos_x}+{win_pos_y}")#sigrze,sigane,marcxena 
#sazgvari, zeda sazgvari

# CREAT AND CONFIG CONTENT
#======================

title = tkinter.Label()
clock = tkinter.Label()

title["text"] = "YOUR TIME IS CURRENTLY:"
title["font"] = ("Arial",14)

clock["text"] = "ERROR"
clock["font"] = ("Arial",36)
clock["bg"] = "#fff"

# PUT THE LABELS ON THE GRID
win.rowconfigure(0, weight = 0)
win.rowconfigure(1, weight = 1)
win.columnconfigure(0, weight = 1)



title.grid(row=0, column=0, pady=20,ipady=5)
clock.grid(row=1, column=0, pady=0,ipadx=10,ipady=5)


#clock.pack()printis magivrad, grid jobia



# CLOCK LOGIC FUNCTION
#================================

def update_time(): 
    clock["text"] = time.strftime("%H:%M:%S")
    win.after(1000,update_time) #kovel 1000milicamshiimeoros funqcia

update_time()


#this will loop everything inside
win.mainloop()#amit mtavrdeba