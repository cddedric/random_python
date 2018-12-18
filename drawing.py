# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 01:38:53 2018

@author: Cuhdols
"""

import turtle

window = turtle.Screen()
turt = turtle.Turtle()
turt.left(90)       #turtle starts center of screen pointed right, 90 left is up
turt.forward(100)   #move forward to draw stem
turt.right(90)      #turn 90 right
turt.circle(10)     #draw a circle 10 units wide ccw starting at 6 o'clock position

for i in range(1,24):   #draws 24 petals to the flower
    turt.left(15)
    turt.forward(50)
    turt.left(157)
    turt.forward(50)

turt.hideturtle() #hides the triangle "turtle"

window.exitonclick()#close window when clicked on