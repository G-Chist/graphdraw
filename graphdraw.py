import time
import turtle as tu
import tkinter as tk
from math import *

def rangevar(var, low, high):
    if var < low:
        var = low
    if var > high:
        var = high
    return var

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
        t.goto(0, i * 60)
        t.goto(5, i * 60)
        t.goto(-5, i * 60)
        t.goto(0, i * 60)
    t.goto(0, 0)
    for i in range(6):
        t.goto(0, -i * 60)
        t.goto(5, -i * 60)
        t.goto(-5, -i * 60)
        t.goto(0, -i * 60)
    t.goto(0, 0)
    for i in range(6):
        t.goto(i * 60, 0)
        t.goto(i * 60, 5)
        t.goto(i * 60, -5)
        t.goto(i * 60, 0)
    t.goto(0, 0)
    for i in range(6):
        t.goto(-i * 60, 0)
        t.goto(-i * 60, 5)
        t.goto(-i * 60, -5)
        t.goto(-i * 60, 0)

    t.penup()

def graph(f, start = -5, end = 5):
    start = rangevar(start, -5, 5)
    end = rangevar(end, -5, 5)
    t.penup()
    for j in [x * 0.1 for x in range(start * 12, end * 12)]:
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

root = tk.Tk()
root.geometry("900x820")
root.title("GraphDraw")
canvas = tk.Canvas(master = root, width = 700, height = 700)
canvas.grid(padx = 2, pady = 0, row=  0, column = 0, rowspan = 10, columnspan = 10, sticky = 'nsew')
t = tu.RawTurtle(canvas)

t.speed(10)

draw_coords()

t.pensize(1)

#Сердечко
graph("sqrt(1 - (-x - 1) ** 2)")
graph("sqrt(1 - (x - 1) ** 2)")
graph("acos(1 + x) - 3.141592653589")
graph("acos(1 - x) - 3.141592653589")

root.mainloop()
