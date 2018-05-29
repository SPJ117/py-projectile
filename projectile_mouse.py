from tkinter import *
import math
window = Tk()

#assign and initialize variables
w=1200
h=600
xlist =[]
ylist=[]
dist=50
originx=200
originy=450

canvas = Canvas(window,width=w,height=h,background='light sky blue')
canvas.grid(columnspan =8)
canvas.create_text(400,50,anchor=W,fill='blue',font=('Helvetica',30),text= 'PROJECTILE SIMULATOR')
canvas.focus_set()

#making grids

nh=int(h/dist)
nw=int(w/dist)
for x in range(nh):
    canvas.create_line(0,(dist*x),w,(dist*x),fill='red',width=1)
for x in range(nw):
    canvas.create_line((dist*x),0,(dist*x),h,fill='black',width=1)
    
canvas.create_line(originx,0,originx,h,fill='black',width=4)
canvas.create_line(0,originy,w,originy,fill='black',width=4)

#clear canvas
def clear():
    canvas.delete('p')
    canvas.delete('l1')
    canvas.delete('bm')
    maxheight.set('')
    maxrange.set('')
    velocityf.set('')
    anglef.set('')

#animate image on trajectory
def animate():
    print('animating now')
    size = len(xlist)
    print('dots in trajectory  =', size)
    x=0
    while (x<size):
        canvas.update()
        canvas.after(30)
        canvas.delete('bm')
        canvas.create_bitmap(originx+xlist[x],originy-ylist[x],bitmap='info',tags='bm')
        x=x+1

#draw trajectory and display projectile's information
def holddrag(event):
    canvas.delete('l1')
    canvas.delete('p')
    global xlist
    global ylist
    ylist.clear()
    xlist.clear()
    x=(event.x)
    y=(event.y)
    length = round(  math.sqrt((x-originx)**2 + (y-originy)**2  )/4,2)
    angle =   round(     180%( math.degrees(math.atan2(y-originy,x-originx))  )  ,2)

    if( angle < 0 ):
        angle=0
    velocityf.set(length)
    anglef.set(angle)
    
    t=0
    time = 2*float(length)*math.sin(math.radians(float(angle)))/10
    maxheight.set(     round( float(length)*float(length) * 0.05 * (math.sin(math.radians(float(angle)))  )**2 ,3)     )
    maxrange.set( round( float(length)*float(length) * 0.1 * (math.sin(2*math.radians(float(angle)))),3  )       )
    while(t<=time):
        sx =  round(float(length)*t*(math.cos(math.radians(float(angle))))*5,2)
        sy = round(((float(length)*t*math.sin(math.radians(float(angle)))  ) - 0.5*10* t*t)*5,2)
        xlist.append(sx)
        ylist.append(sy)
        canvas.create_oval(  originx-3 + sx , originy -3 -sy, originx +3 +sx , originy+3 -sy ,fill='green',tags='p')
        t=t+0.1
    canvas.create_line(originx,originy,x,y,width=2,fill='purple',tags='l1')
def o():
    print(var.get())
    if(var.get()=='Level 2'):
        canvas.create_oval(600-10,180-10,600+10,180+10,fill='yellow',tags='o')
        canvas.create_polygon(300,450,550,200,650,200,900,450,tags='o1')
    else:
        canvas.delete('o')
        canvas.delete('o1')

#menubar
menubar = Menu()
menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=menu)
menu.add_command(label="New", command = clear)
window.config(menu=menubar)

#widgets - buttons and labels
canvas.create_bitmap(originx,originy,bitmap='info',tags='bm')
Label(window, text='Your Velocity').grid(row=1,column = 0,sticky=E)
Label(window, text='Your Angle').grid(row=2, column = 0,sticky=E)
Label(window, text='Maximum Height').grid(row=1, column = 2,sticky=E)
Label(window, text='Range').grid(row=2,column = 2,sticky=E)

velocityf = StringVar()
anglef = StringVar()
maxheight = StringVar()
maxrange = StringVar()
var = StringVar(window)
var.set('Level 1')
op = OptionMenu(window, var, 'Level 1','Level 2','Level 3').grid(row=1,column=4,sticky=W,pady=10)
button = Button(window, text="OK", command=o).grid(row=1,column=5,sticky=W,pady=10)


e1 = Entry(window, textvariable =velocityf)
e2 = Entry(window, textvariable =anglef)
e1.grid(row = 1, column = 1,sticky=W,padx = 10)
e2.grid(row = 2, column = 1,sticky =W,padx = 10)
e3 = Entry(window , textvariable =maxheight)
e4 = Entry(window , textvariable =maxrange)
e3.grid(row = 1, column = 3,sticky=W,padx = 10)
e4.grid(row = 2, column = 3,sticky =W,padx = 10)

Button(window, text='PROJECT', command = animate).grid(rowspan = 2 , row=1,  column = 2,sticky= W, pady=10)
canvas.bind('<B1-Motion>',(holddrag))

window.mainloop()
