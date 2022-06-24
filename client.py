from tkinter import *
import threading
from time import strftime
import socket

BACKGROUND_COLOR = "#ebedef"
TEXT_SLIDING_COLOR = "#800000"


# ---------------------------- FUNCTIONS ------------------------------- #

def thread():
    threading.Thread(target=ordering).start()


# Function for connection with server
def ordering():
    pizza = select()

    order = name.get() + " " + surname.get() + " (" + adresa.get() + ", " + number.get() + ") - " + pizza

    if on_side1.get() == 1:
        order += " + Mayonnaise"

    if on_side2.get() == 1:
        order += " + Ketchup"

    if on_side3.get() == 1:
        order += " + Oregano"

    s = socket.socket()
    s.connect(("localhost", 12345))
    s.send(order.encode())
    strGet = s.recv(1024).decode()


# Function for sliding text
def shift():
    x1, y1, x2, y2 = canvasText.bbox("marquee")
    if x2 < 0 or y1 < 0:
        x1 = canvasText.winfo_width()
        y1 = canvasText.winfo_height() // 2
        canvasText.coords("marquee", x1, y1)
    else:
        canvasText.move("marquee", -2, 0)
    canvasText.after(1000 // fps, shift)


# Function for time
def my_time():
    time_string = strftime('%H:%M:%S %p \n %A')
    timee.config(text=time_string)
    timee.after(1000, my_time)


# Function for segregate checked pizza
def select():
    reslist = list()
    seleccion = Lb1.curselection()
    for i in seleccion:
        entrada = Lb1.get(i)
        reslist.append(entrada)
    pizzaa = ', '.join(reslist)
    return pizzaa

# ---------------------------- UI SETUP ------------------------------- #


# Making GUI
window = Tk()
window.config(width=600, height=700, bg=BACKGROUND_COLOR)
window.title("Pizza ordering")

# Making Canvas for Logo
canvasLogo = Canvas(window, width=200, height=220)
img = PhotoImage(file="./resources/pizza_logo.png")
canvasLogo.create_image(100, 110, image=img)
canvasLogo.grid(row=0, column=3)

# Making Canvas for sliding text
canvasText = Canvas(window, width=400, height=220, bg=BACKGROUND_COLOR)
text_var = "Welcome to the best PIZZA order application !!!"
text = canvasText.create_text(0, -2000, text=text_var, font=('Times', 25, 'bold'),
                              fill=TEXT_SLIDING_COLOR, tags=("marquee",), anchor='w')
canvasText.grid(row=0, column=0, columnspan=3, sticky='ew')
fps = 40

# Displaying time on screen
timee = Label(window, font=('Times', 13, 'bold'), bg=BACKGROUND_COLOR)
timee.grid(row=1, column=3)

name = StringVar()
surname = StringVar()
adresa = StringVar()
number = StringVar()
on_side1 = IntVar()
on_side2 = IntVar()
on_side3 = IntVar()
valores = StringVar()


Label(text="Name:", font=('Times', 15), bg=BACKGROUND_COLOR).grid(row=1, column=1, pady=(15, 0))
Entry(window, bg="#c3c3c3", cursor="pencil", width=25, textvariable=name).grid(row=1, column=2,
                                                                               padx=(0, 50), pady=(15, 0))

Label(text="Surname:", font=('Times', 15), bg=BACKGROUND_COLOR).grid(row=2, column=1, pady=(5, 0))
Entry(window, bg="#c3c3c3", cursor="pencil", width=25, textvariable=surname).grid(row=2, column=2,
                                                                                  padx=(0, 50), pady=(5, 0))

Label(text="Address:", font=('Times', 15), bg=BACKGROUND_COLOR).grid(row=3, column=1, pady=(5, 0))
Entry(window, bg="#c3c3c3", cursor="pencil", width=30, textvariable=adresa).grid(row=3, column=2,
                                                                                 padx=(0, 50), pady=(5, 0))

Label(text="Phone Number:", font=('Times', 15), bg=BACKGROUND_COLOR).grid(row=4, column=1, pady=(5, 0))
phone_entry = Entry(window, bg="#c3c3c3", cursor="pencil", width=30, textvariable=number)
phone_entry.grid(row=4, column=2, padx=(0, 50), pady=(5, 0))
phone_entry.insert(0, "+381 6")

Label(text="Choose pizza: ", font=('Times', 15), bg=BACKGROUND_COLOR).grid(row=5, column=1, pady=(5, 0))
Lb1 = Listbox(window, selectmode=MULTIPLE, height=11, font=('Times', 12, "bold"), cursor="plus", listvariable=valores)
Lb1.insert(0, "Capricciosa 32cm")
Lb1.insert(1, "Capricciosa 46cm")
Lb1.insert(2, "Pepperoni 32cm")
Lb1.insert(3, "Pepperoni 46cm")
Lb1.insert(4, "BBQ_Chicken 32cm")
Lb1.insert(5, "BBQ_Chicken 46cm")
Lb1.insert(6, "Veggie 32cm")
Lb1.insert(7, "Veggie 46cm")
Lb1.insert(8, "Margherita 32cm")
Lb1.insert(9, "Margherita 46cm")
Lb1.grid(row=5, column=2, pady=(5, 0))


Label(window, text="Add:", font=('Times', 15), bg=BACKGROUND_COLOR).grid(row=6, column=0, pady=(5, 0), padx=(60, 20))
Checkbutton(window, text="Mayonnaise", variable=on_side1, onvalue=1, offvalue=0, font=('Times', 13),
            bg=BACKGROUND_COLOR).grid(row=6, column=1, pady=(5, 0))
Checkbutton(window, text="Ketchup", variable=on_side2, onvalue=1, offvalue=0, font=('Times', 13),
            bg=BACKGROUND_COLOR).grid(row=6, column=2, pady=(5, 0))
Checkbutton(window, text="Oregano", variable=on_side3, onvalue=1, offvalue=0, font=('Times', 13),
            bg=BACKGROUND_COLOR).grid(row=6, column=3, pady=(5, 0))

Button(window, text="Submit", relief=GROOVE, width=13, command=thread).grid(row=7, column=1, columnspan=2, pady=(15, 20))

threading.Thread(target=my_time).start()
threading.Thread(target=shift).start()

window.mainloop()
