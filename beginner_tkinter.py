#from curses import BUTTON1_CLICKED
import tkinter as tk
#import tkinter.

window = tk.Tk()
window.title("Window 1")
text = tk.Label(text = "This is a window", width = 12, fg = "blue", bg = "black")
text.pack()
text = tk.Label(text = "Name")
entry = tk.Entry()
text.pack()
entry.pack()
enter = tk.Button(text = "Enter", fg = "red")
enter.pack()
name = entry.get()
print(name)
full = tk.Text()
full.pack()
window.mainloop()
