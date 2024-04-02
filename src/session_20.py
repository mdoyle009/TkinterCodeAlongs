import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True) 
#fills frame to the whole window X and Y axis and packs to the left
#height and width value still give initial window height and width before expanding

frame2 = tk.Frame(master=window, width=100, bg="yellow")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=25, bg="blue")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()



window2 = tk.Tk()

frame = tk.Frame(master=window2, width=150, height=150, borderwidth=2, bg="black")
frame.pack()

label1 = tk.Label(master=frame, text="I'am at (0,0)", bg="red")
label1.place(x=0, y=0)
#(0,0) is at top left corner of frame. Negative x and y is left and up (outside of frame), positive is right and down
label2 = tk.Label(master=frame, text="I'm at (75,75)", bg="yellow")
label2.place(x=75, y=75)

window2.mainloop()



window3 = tk.Tk()

for i in range(3): #just to create 9 frames faster
    window3.columnconfigure(i, weight=1, minsize=75)
    window3.rowconfigure(i, weight=1, minsize=50)
    for j in range(3):
        frame4 = tk.Frame(master=window3, relief="raised", borderwidth=1)
        frame4.grid(row=i, column=j, padx=5, pady=5) #pad adds some pixel buffer between frames
        label = tk.Label(master=frame4, text=f"Row {i}\nColumn {j}")
        label.pack(padx=5, pady=5) #adds space around label from frame

window3.mainloop()



window4 = tk.Tk()
window4.rowconfigure(0, minsize=250, weight=1)
window4.columnconfigure([0, 1, 2, 3], minsize=250, weight=1) #we have 4 rows, so configure all rows

labelA = tk.Label(master=window4, text="A", bg="red")
labelA.grid(row=0, column=0) 

#sticky north (n), south (s), east (e), west (w), northeast (ne), etc

labelB = tk.Label(master=window4, text="B", bg="yellow")
labelB.grid(row=0, column=1, sticky="ew")

labelC = tk.Label(master=window4, text="C", bg="blue")
labelC.grid(row=0, column=2, sticky="ns")

labelD = tk.Label(master=window4, text="D", bg="green")
labelD.grid(row=0, column=3, sticky="nsew")

window4.mainloop()