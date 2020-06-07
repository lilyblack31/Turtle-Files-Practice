#! /usr/bin/env python3
from turtle import Turtle, Screen

""" Creates a design that has a spiral inside a spiral """

def draw_square(turtle_artist):
    """ Draws a square to contain the spiral """
    for numberlimit in range(36):
        for number in range(4):
            turtle_artist.forward(175)
            turtle_artist.right(90)
        turtle_artist.right(10)

def draw_spiral(turtle_artist):
    """ Draws a spiral using the squares """
    size = 1
    for number in range(300):
        turtle_artist.forward(size)
        turtle_artist.right(91)
        size += 1

def define_and_draw():
    """ Defines the two turtle objects and draws a spiral inside a spiral """
    # Artist Turtle 1
    turtle_artist_1 = Turtle()
    turtle_artist_1.color("Red")
    turtle_artist_1.pensize(2)
    turtle_artist_1.speed("fastest")

    draw_square(turtle_artist_1)

    # Artist Turtle 2
    turtle_artist_2 = Turtle()
    turtle_artist_2.color("Black")
    turtle_artist_2.pensize(2)
    turtle_artist_2.speed("fast")

    draw_spiral(turtle_artist_2)


window = Screen()
define_and_draw()
window.exitonclick()
