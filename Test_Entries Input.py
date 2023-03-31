#Import tkinter library
from tkinter import *
#Create an instance of tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x350")
#Crate a Label widget
label1= Label(win, text="Box1")
label1.pack()
label2= Label(win, text= "
Keep
Learning", bd=1, relief= "solid",font= ("Helvetica 20"), justify= RIGHT)
label2.pack()
Label(win, text= "Box2").pack()
label3= Label(win, text="
Learning
Makes
Perfect", bd=1, relief="solid", font=('Helvetica 20'), justify= LEFT)
label3.pack()
win.mainloop()