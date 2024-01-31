
from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Fish Price Calculation Program for Pumpuang Truck')
GUI.geometry('500x300')

bg = PhotoImage(file='Truck-icon.png')
#bg = PhotoImage(file='C:\\Users\\mamak\\Desktop\\Basic Python\\EP5\\Truck-icon.png')
#bg = PhotoImage(file=r'C:\Users\mamak\Desktop\Basic Python\EP5\Truck-icon.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='Please fill in amount of fish in kg', font=(None,20))
L.pack()

v_quantity = StringVar() #Variable from the input text
E1 = ttk.Entry(GUI, textvariable=v_quantity, font = (None,20))
E1.pack()

def Cal():
    try:  
        quan = float(v_quantity.get())
        calc = quan * 39 # 39 Baht/kg
        messagebox.showinfo('Total price','Total fish price is {} baht'.format(calc))
        v_quantity.set('')
        E1.focus()
    except: 
        messagebox.showwarning('Wrong input', 'Please fill in only numbers')
        v_quantity.set('')
        E1.focus()

B = ttk.Button(GUI,text='Calculate',command=Cal)
B.pack(ipadx=30, ipady=20, pady=20) #ipadx/y increase width x/y

GUI.mainloop() #for continuous running