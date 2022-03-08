import time
import turtle as tu
from tkinter import *
from math import *

def rangevar(var, low, high):
    if var < low:
        var = low
    if var > high:
        var = high
    return var

def isnum(var):
    try:
        a = float(var) - 1
        return True
    except TypeError and ValueError:
        return False

def create_canvas():
    global t
    canvas = Canvas(master = root, width = 600, height = 600)
    canvas.grid(padx = 2, pady = 0, row = 0, column = 0, rowspan = 20, columnspan = 20, sticky = 'nsew')
    t = tu.RawTurtle(canvas)
    t.speed(10)
    t.pensize(1)
    draw_coords()

def draw_coords():

    t.pensize(2)

    t.goto(0, 320)
    t.goto(t.pos()[0] - 5, t.pos()[1] - 10)
    t.goto(0, 320)
    t.goto(t.pos()[0] + 5, t.pos()[1] - 10)
    t.goto(0, 320)

    t.goto(0, -320)

    t.goto(0, 0)

    t.goto(-320, 0)

    t.goto(320, 0)
    t.goto(t.pos()[0] - 10, t.pos()[1] + 5)
    t.goto(320, 0)
    t.goto(t.pos()[0] - 10, t.pos()[1] - 5)
    t.goto(320, 0)

    t.goto(0, 0)

    t.pensize(1)
    for i in range(6):
        t.goto(0, i * 50)
        t.goto(5, i * 50)
        t.goto(-5, i * 50)
        t.goto(0, i * 50)
    t.goto(0, 0)
    for i in range(6):
        t.goto(0, -i * 50)
        t.goto(5, -i * 50)
        t.goto(-5, -i * 50)
        t.goto(0, -i * 50)
    t.goto(0, 0)
    for i in range(6):
        t.goto(i * 50, 0)
        t.goto(i * 50, 5)
        t.goto(i * 50, -5)
        t.goto(i * 50, 0)
    t.goto(0, 0)
    for i in range(6):
        t.goto(-i * 50, 0)
        t.goto(-i * 50, 5)
        t.goto(-i * 50, -5)
        t.goto(-i * 50, 0)

    t.penup()

def graph():
    print("Plotting started")
    for i in range(1, 11):
        exec("global f; f = graphfield" + str(i) + ".get()")
        print(f)
        if f != "":
            exec("global st; st = graphstart" + str(i) + ".get()")
            exec("global en; en = graphend" + str(i) + ".get()")
            start = -5 if not isnum(st) else float(st)
            end = 5 if not isnum(en) else float(en)
            start = rangevar(start, -5, 5)
            end = rangevar(end, -5, 5)
            t.penup()
            for j in [x * 0.1 for x in range(int(start * 12), int(end * 12))]:
                try:
                    expr = round(eval(''.join([i if i != "x" else str(j) for i in f])) * 50)
                    t.goto(j * 50, rangevar(expr, -3000, 3000))
                    t.pendown()
                    if not expr in range(-500, 500):
                        t.penup()
                    print("X: ", j, "; Y: ", eval(''.join([i if i != "x" else str(j) for i in f])))
                except ValueError:
                    print("ValueError")
                except SyntaxError:
                    print("SyntaxError")
                except ZeroDivisionError:
                    print("ZeroDivisionError")
                    t.penup()
            print("Finished!")
            t.penup()
        t.goto(0, 0)

root = Tk()
root.geometry("1200x900")
root.title("GraphDraw")

graphfield1 = Entry(root, width = 40)
graphfield1.grid(padx = 5, pady = 5, row = 0, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from1 = Label(root, text = "from")
from1.grid(padx = 5, pady = 5, row = 0, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart1 = Entry(root, width = 15)
graphstart1.grid(padx = 5, pady = 5, row = 0, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to1 = Label(root, text = "to")
to1.grid(padx = 5, pady = 5, row = 0, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend1 = Entry(root, width = 15)
graphend1.grid(padx = 5, pady = 5, row = 0, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield2 = Entry(root, width = 40)
graphfield2.grid(padx = 5, pady = 5, row = 1, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from2 = Label(root, text = "from")
from2.grid(padx = 5, pady = 5, row = 1, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart2 = Entry(root, width = 15)
graphstart2.grid(padx = 5, pady = 5, row = 1, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to2 = Label(root, text = "to")
to2.grid(padx = 5, pady = 5, row = 1, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend2 = Entry(root, width = 15)
graphend2.grid(padx = 5, pady = 5, row = 1, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield3 = Entry(root, width = 40)
graphfield3.grid(padx = 5, pady = 5, row = 2, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from3 = Label(root, text = "from")
from3.grid(padx = 5, pady = 5, row = 2, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart3 = Entry(root, width = 15)
graphstart3.grid(padx = 5, pady = 5, row = 2, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to3 = Label(root, text = "to")
to3.grid(padx = 5, pady = 5, row = 2, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend3 = Entry(root, width = 15)
graphend3.grid(padx = 5, pady = 5, row = 2, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield4 = Entry(root, width = 40)
graphfield4.grid(padx = 5, pady = 5, row = 3, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from4 = Label(root, text = "from")
from4.grid(padx = 5, pady = 5, row = 3, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart4 = Entry(root, width = 15)
graphstart4.grid(padx = 5, pady = 5, row = 3, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to4 = Label(root, text = "to")
to4.grid(padx = 5, pady = 5, row = 3, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend4 = Entry(root, width = 15)
graphend4.grid(padx = 5, pady = 5, row = 3, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield5 = Entry(root, width = 40)
graphfield5.grid(padx = 5, pady = 5, row = 4, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from5 = Label(root, text = "from")
from5.grid(padx = 5, pady = 5, row = 4, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart5 = Entry(root, width = 15)
graphstart5.grid(padx = 5, pady = 5, row = 4, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to5 = Label(root, text = "to")
to5.grid(padx = 5, pady = 5, row = 4, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend5 = Entry(root, width = 15)
graphend5.grid(padx = 5, pady = 5, row = 4, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield6 = Entry(root, width = 40)
graphfield6.grid(padx = 5, pady = 5, row = 5, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from6 = Label(root, text = "from")
from6.grid(padx = 5, pady = 5, row = 5, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart6 = Entry(root, width = 15)
graphstart6.grid(padx = 5, pady = 5, row = 5, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to6 = Label(root, text = "to")
to6.grid(padx = 5, pady = 5, row = 5, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend6 = Entry(root, width = 15)
graphend6.grid(padx = 5, pady = 5, row = 5, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield7 = Entry(root, width = 40)
graphfield7.grid(padx = 5, pady = 5, row = 6, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from7 = Label(root, text = "from")
from7.grid(padx = 5, pady = 5, row = 6, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart7 = Entry(root, width = 15)
graphstart7.grid(padx = 5, pady = 5, row = 6, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to7 = Label(root, text = "to")
to7.grid(padx = 5, pady = 5, row = 6, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend7 = Entry(root, width = 15)
graphend7.grid(padx = 5, pady = 5, row = 6, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield8 = Entry(root, width = 40)
graphfield8.grid(padx = 5, pady = 5, row = 7, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from8 = Label(root, text = "from")
from8.grid(padx = 5, pady = 5, row = 7, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart8 = Entry(root, width = 15)
graphstart8.grid(padx = 5, pady = 5, row = 7, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to8 = Label(root, text = "to")
to8.grid(padx = 5, pady = 5, row = 7, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend8 = Entry(root, width = 15)
graphend8.grid(padx = 5, pady = 5, row = 7, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield9 = Entry(root, width = 40)
graphfield9.grid(padx = 5, pady = 5, row = 8, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from9 = Label(root, text = "from")
from9.grid(padx = 5, pady = 5, row = 8, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart9 = Entry(root, width = 15)
graphstart9.grid(padx = 5, pady = 5, row = 8, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to9 = Label(root, text = "to")
to9.grid(padx = 5, pady = 5, row = 8, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend9 = Entry(root, width = 15)
graphend9.grid(padx = 5, pady = 5, row = 8, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

graphfield10 = Entry(root, width = 40)
graphfield10.grid(padx = 5, pady = 5, row = 9, column = 21, rowspan = 1, columnspan = 3, sticky = 'nsew')
from10 = Label(root, text = "from")
from10.grid(padx = 5, pady = 5, row = 9, column = 24, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphstart10 = Entry(root, width = 15)
graphstart10.grid(padx = 5, pady = 5, row = 9, column = 25, rowspan = 1, columnspan = 2, sticky = 'nsew')
to10 = Label(root, text = "to")
to10.grid(padx = 5, pady = 5, row = 9, column = 27, rowspan = 1, columnspan = 1, sticky = 'nsew')
graphend10 = Entry(root, width = 15)
graphend10.grid(padx = 5, pady = 5, row = 9, column = 28, rowspan = 1, columnspan = 2, sticky = 'nsew')

buildbtn = Button(root, width = 11, height = 2, text = "Build graphs", command = graph)
buildbtn.grid(padx = 5, pady = 5, row = 10, column = 21, rowspan = 1, columnspan = 1, sticky = 'nsew')

clearbtn = Button(root, width = 11, height = 2, text = "Clear graphs", command = create_canvas)
clearbtn.grid(padx = 5, pady = 5, row = 12, column = 21, rowspan = 1, columnspan = 1, sticky = 'nsew')

create_canvas()

root.mainloop()
