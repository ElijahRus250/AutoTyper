import pyautogui 
import time
import tkinter as tk
from tkinter import *
print('Booting up....')
root= tk.Tk()
root.title('Auto Typer')
# p1 = PhotoImage(file = 'C:/Users/Elija/OneDrive/Desktop/Python Auto Typer/typing.png')
# # Icon set for program window
# root.iconphoto(False, p1)

# root.iconbitmap('typing.png')
canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Auto Typer')
label1.config(font=('Courier', 14, 'bold'))
canvas1.create_window(200, 46, window=label1)

label2 = tk.Label(root, text='Paste your Text:')
label2.config(font=('Courier', 10))
canvas1.create_window(200, 100, window=label2)


entry1 = tk.Entry (root) 


canvas1.create_window(200, 100, window=entry1, height=50, width=150)
print('Finished startup... The program should now be open...')

def typeMessage ():
    print('Typing will begin in 5 seconds... Move into a text box')
    x = entry1.get()
    
    time.sleep(5)
    print('Starting typing at a 0.10 interval..')
    pyautogui.typewrite(x, interval=0.10)
    print('Typing is now complete!')

    
button1 = tk.Button(text='Click to type', command=typeMessage, bg='brown', fg='white', font=('helvetica', 11, 'bold'))
canvas1.create_window(200, 150, window=button1)

root.mainloop()
