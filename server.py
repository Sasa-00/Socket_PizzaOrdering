import socket
from tkinter import *
import threading
import time
import SQL
import sqlite3


def server():
    global order
    s = socket.socket()
    s.bind(("localhost", 12345))
    s.listen()
    while True:

        # Server receiving and writing orders
        conn, adr = s.accept()
        str_order = conn.recv(1024).decode()
        named_tuple = time.localtime()
        time_string = time.strftime("%A - %H:%M:%S", named_tuple)
        text.insert("0.0", time_string + "  " + str_order+"\n\n")
        text.insert("0.0", "SERVER:waiting..." + "\n")

        # Separating text to maintain base
        order_lst = str_order.split(" - ")
        if "+" in order_lst[1]:
            order_lst = (order_lst[1].split(" + "))[0]
            order_lst = order_lst.split(", ")
            for ordd in order_lst:
                order = ordd
                order = order.split(" ")
                try:
                    SQL.creating_table()
                    SQL.deleting_from_table(str(order[0]), str(order[1]))

                except sqlite3.OperationalError:
                    SQL.deleting_from_table(str(order[0]), str(order[1]))
        else:
            order_lst = order_lst[1]
            order_lst = order_lst.split(", ")
            for ordd in order_lst:
                order = ordd
                order = order.split(" ")
                try:
                    SQL.creating_table()
                    SQL.deleting_from_table(str(order[0]), str(order[1]))

                except sqlite3.OperationalError:
                    SQL.deleting_from_table(str(order[0]), str(order[1]))


# New tkinter instance (window)
window = Tk()

window.config(width=600, height=700, )
Label(text="Received orders :", font=('Times', 20)).grid(row=0, column=0)

text = Text(window, font=('Times', 15))
text.grid(row=1, column=0)


threading.Thread(target=server).start()
window.mainloop()
