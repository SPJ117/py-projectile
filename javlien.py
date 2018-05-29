from tkinter import *
import math
window = Tk()

#variables
w=1200
h=600
canvas = Canvas(window,width=w,height=h,background='sky blue')
canvas.grid(columnspan =5)

dist=50
nh=int(h/dist)
nw=int(w/dist)

#making gridlines
for x in range(nh):
    canvas.create_line(0,(dist*x),w,(dist*x),fill='red',width=2)
for x in range(nw):
    canvas.create_line((dist*x),0,(dist*x),h,fill='black',width=2)
canvas.create_line((dist),0,(dist),h,fill='black',width=4)
canvas.create_line(0,(h-dist),w,(h-dist),fill='red',width=4)
          
#plot graph
def graph():
    x=0
    v1=velocity.get()
    v2=angle.get()
    time = 2*float(v1)*math.sin(math.radians(float(v2)))/10
    #print(v1,v2)
    maxheight.set(     round( float(v1)*float(v1) * 0.05 * (math.sin(math.radians(float(v2)))  )**2 ,3)     )
    maxrange.set( round( float(v1)*float(v1) * 0.1 * (math.sin(2*math.radians(float(v2)))),3  )       )
    
    while(x<=time):
        sx =  round(float(v1)*x*(math.cos(math.radians(float(v2))))*5,2)
        sy = round(((float(v1)*x*math.sin(math.radians(float(v2)))  ) - 0.5*10* x*x)*5,2)
        canvas.create_oval(  50-3 + sx , 550 -3 -sy, 50 +3 +sx , 550+3 -sy ,fill='green',tags='p')
        #print(round(x,2), sx , sy)
        x=x+0.1
		
#clear canvas
def clear():
    canvas.delete('p')
    maxheight.set('')
    maxrange.set('')
    velocity.set('')
    angle.set('')
canvas.focus_set()
global sx
global sy

#menubar
menubar = Menu()
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=menu)
menu.add_command(label="New", command = clear)
window.config(menu=menubar)

#widgets - buttons and labels
Label(window, text='Enter Velocity').grid(row=1,column = 0,sticky=E)
Label(window, text='Enter Angle').grid(row=2, column = 0,sticky=E)
Label(window, text='Maximum Height').grid(row=1, column = 2,sticky=E)
Label(window, text='Range').grid(row=2,column = 2,sticky=E)

velocity = StringVar()
angle = StringVar()
maxheight = StringVar()
maxrange = StringVar()

e1 = Entry(window, textvariable =velocity)
e2 = Entry(window, textvariable =angle)
e1.grid(row = 1, column = 1,sticky=W,padx = 10)
e2.grid(row = 2, column = 1,sticky =W,padx = 10)
e3 = Entry(window , textvariable =maxheight)
e4 = Entry(window , textvariable =maxrange)
e3.grid(row = 1, column = 3,sticky=W,padx = 10)
e4.grid(row = 2, column = 3,sticky =W,padx = 10)
Button(window, text='PROJECT', command = graph).grid(rowspan = 2 , row=1,  column = 2,sticky= W, pady=10)

window.mainloop()
