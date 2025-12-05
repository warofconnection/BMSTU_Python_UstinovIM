from tkinter import *
from tkinter.messagebox import *
from math import sin,cos,pi,exp

ID1=0
ID2=0

def drawfunction():
    Xb = MaxX//2
    Xe = MaxY//2
    R = 100
    cv.create_arc(100, 100, 360, 360, style = 'arc', start = 0, extent = 360, outline = 'red', fill = 'blue')
def showXY(ivent):#Вывод осей на полотно (прицел)
    global ID1,ID2
    x=ivent.x
    y=ivent.y
    cv.delete(ID1)
    cv.delete(ID2)
    ID1 = cv.create_line(0, y, MaxX, y, dash=(3, 5), fill=('black'))
    ID2 = cv.create_line(x, 0, x, MaxY, dash=(3, 5), fill=('black'))

def window_delete():
    if askyesno("ВЫХОД","Вы уверенны, что хотите выйти?", ):
        root.destroy()
root = Tk()
root.title("Графика")
# root.protocol('WM_DELETE_WINDOW', window_deleted)
root.resizable(False,False)
Kp = 0.7
MaxX=root.winfo_screenwidth()*Kp
MaxY=root.winfo_screenheight()*Kp

cv = Canvas(root, width = MaxX, height = MaxY, bg = "white")
cv.grid(row = 0, columnspan = 9)
cv.bind('<Button-1>', showXY)
cv.bind('<Button-1>', drawfunction)
root.mainloop()