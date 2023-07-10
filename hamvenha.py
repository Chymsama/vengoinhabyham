#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle

def draw_house(x, y):
    # Khởi tạo màn hình đồ họa
    screen = turtle.Screen()
    screen.bgcolor('pink')

    # Vẽ ngôi nhà
    house = turtle.Turtle()
    house.color('white')
    house.fillcolor('white')
    house.penup()
    house.goto(x, y)
    house.pendown()
    house.begin_fill()
    for _ in range(4):
        house.forward(200)
        house.left(90)
    house.end_fill()

    roof = turtle.Turtle()
    roof.color('red')
    roof.fillcolor('red')
    roof.penup()
    roof.goto(x + 200, y + 50)
    roof.pendown()
    roof.begin_fill()
    roof.goto(x + 100, y + 150)
    roof.goto(x, y + 50)
    roof.end_fill()

    # Vẽ cửa sổ
    window = turtle.Turtle()
    window.color('lightblue')
    window.fillcolor('lightblue')

    # Vẽ cửa sổ bên trái
    window.penup()
    window.goto(x + 25, y - 50)
    window.pendown()
    window.begin_fill()
    for _ in range(4):
        window.forward(60)
        window.left(90)
    window.end_fill()

    # Vẽ cửa sổ bên phải
    window.penup()
    window.goto(x + 125, y - 50)
    window.pendown()
    window.begin_fill()
    for _ in range(4):
        window.forward(60)
        window.left(90)
    window.end_fill()

    turtle.done()


draw_house(-50,-100)

