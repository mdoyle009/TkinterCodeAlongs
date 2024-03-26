import tkinter as tk
# now you can just type "tk" instead of "tkinter"

window = tk.Tk()
window.title("Tkinter Code Along")
#creates graphical interface, saved to variable for easy access

label1 = tk.Label(
    window,
    text = "Hello, Tkinter",
    foreground = "yellow",
    background = "#000000",
    width = 23,
    height = 10
    )
label1.pack()
#creates a label in window with that text, at the top and centered (pack)
#you can also for bg/fg instead of background/foreground

button1 = tk.Button(
    window,
    text = "Click me!"
    )
button1.pack()

entry1 = tk.Entry(window)
entry1.pack()
entry1.insert(0, "Myeheheh")
entry1.insert(8, "Wow")
entry1.delete(8, tk.END)
text_input = entry1.get()
print(text_input)

window.mainloop()