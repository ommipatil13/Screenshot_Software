import tkinter as tk
import pyautogui

root= tk.Tk()

size1 = tk.Canvas(root, width = 300, height = 300)
size1.pack()

def takesnap():

       screenshot = pyautogui.screenshot()
       screenshot.save(r'C:\\Users\\DELL\\Desktop\\dreamsnap.png')
    
Button1 = tk.Button(text='Take Screenshot', command=takesnap, bg='blue', fg='white', font=10)
size1.create_window(150, 150, window=Button1)

root.mainloop()