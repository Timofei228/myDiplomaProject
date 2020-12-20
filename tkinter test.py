from tkinter import *

root = Tk()

c = Canvas(root, width=200, height=200, bg='white')
c.pack()

c.create_oval(10, 10, 190, 190,
              fill='lightgrey',
              outline='white')
c.create_arc(10, 10, 190, 190,
             start=0, extent=60,
             fill='lightgreen')
c.create_arc(10, 10, 190, 190,
             start=60, extent=60,
             fill='red')
c.create_arc(10, 10, 190, 190,
             start=120, extent=60,
             fill='black')
c.create_arc(10, 10, 190, 190,
             start=180, extent=60,
             fill='blue')
c.create_arc(10, 10, 190, 190,
             start=240, extent=60,
             fill='orange')
c.create_arc(10, 10, 190, 190,
             start=300, extent=60,
             fill='purple')
root.mainloop()