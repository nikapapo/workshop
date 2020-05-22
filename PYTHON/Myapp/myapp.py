# Import
import tkinter as tk
import string
import random



# LOGIC

def generate_password():
    password = []

    for x in range(4):
        alphabet =random.choice(string.ascii_letters)
        symbols  =random.choice(string.punctuation)
        numbers  =random.choice(string.digits)
        password.append(alphabet)
        password.append(symbols)
        password.append(numbers)
    
    y="".join(str(x)for x in password)
    textbox.insert(tk.INSERT,y)
    return(x)
# for copy a password you must select it with left mousbutton, then ctr+c
# i didn't found any other solution
    


#  WINDOW
#===========================
HEIGHT = 300
WIDTH = 400

root =tk.Tk()
root.title("Password Generator")

canvas = tk.Canvas(root, height = HEIGHT, width= WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="blue", bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.25,anchor='n')

textbox = tk.Text(frame,font=('Arial',14))
textbox.place(relwidt=0.65,relheight=1.)


button = tk.Button(frame,text="Generate", font=('Arial',12),bg="white",command=generate_password)
button.place(relx=0.7,relheight=1.,relwidt=0.3)






root.mainloop()