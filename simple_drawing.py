#!/usr/bin/env python3
import turtle

""" A simple program to draw a basic figure using the turtle module """

artist = turtle.Turtle()
artist.speed("fastest")

def draw(drawing_color, drawing_size):
    """ Function to help draw the required shapes """
    for size1 in range(1, 72):
        for size2 in range(1, 6):
            artist.color(drawing_color)
            artist.forward(drawing_size)
            artist.left(144)
        artist.left(5)

def main():
    instructions = [
        ("Orange", 300),
        ("Red", 200),
        ("Blue", 150),
        ("Yellow", 75),
    ]
    for color, size in instructions:
        draw(color, size)

main()
