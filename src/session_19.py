import tkinter as tk

window = tk.Tk()

text_box = tk.Text()
text_box.pack()
text_box.insert("1.0", "Hello") #Text box starts at line 1, character 0
text_box.insert("2.0", "\nGoodbye") #only one line exists, so create second line with \n
text_box.insert(tk.END, "\nI'm at the end!")

text = text_box.get("1.0")
print(text)
text = text_box.get("2.0", "2.7")
print(text)
text = text_box.get("1.0", tk.END)
print(text)

text_box.delete("1.0", "2.0") #To clear the whole line, need to grab escape character

window.mainloop()

window2 = tk.Tk()
frameA = tk.Frame(master=window2, relief="raised", borderwidth=5)
frameB = tk.Frame(master=window2, relief="sunken", borderwidth=5)
labelA = tk.Label(master=frameA, text="I am in Frame A", bg="red")
labelB = tk.Label(master=frameB, text="I am in Frame B", bg="blue")
labelA.pack()
labelB.pack()
frameA.pack()
frameB.pack()
border_effects = {
    "flat":tk.FLAT,
    "sunken":tk.SUNKEN,
    "raised":tk.RAISED,
    "groove":tk.GROOVE,
    "ridge":tk.RIDGE,
    "solid":tk.SOLID
}
window2.mainloop()