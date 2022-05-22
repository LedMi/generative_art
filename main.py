#!/usr/bin/env python

import random
import math
import cairo

WIDTH, HEIGHT = 512, 512

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

pat = cairo.LinearGradient(0.0, 0.0, 1.0, 1.0)
pat.add_color_stop_rgba(0.91, 0, 0, 0, 0.01)  # First stop, 50% opacity
pat.add_color_stop_rgba(0.01, 0.5, 1, 1, 0.2)  # Last stop, 100% opacity
pat.add_color_stop_rgba(0.001, 0, 0.5, 1, 0.01)  # Last stop, 100% opacity

ctx.rectangle(0, 0, 10, 10)  # Rectangle(x0, y0, x1, y1)
ctx.set_source(pat)
ctx.fill()

ctx.translate(0.1, 0.1)  # Changing the current transformation matrix

ctx.move_to(0.0, 0.0)
# Arc(cx, cy, radius, start_angle, stop_angle)

r = random.randrange(6, 35)
print(r)

def triangle(x:float,y:float,z:float,c:float, k1:float, k2:float, k3:float):
    ctx.set_line_width(0.001)
    ctx.new_sub_path()
    ctx.set_source_rgb(k1, k2, k3)
    ctx.line_to(z/21+c, x/20+c)
    ctx.line_to(x/20+c, y/15+c)
    ctx.line_to(y/15+c, z/21+c)
    ctx.line_to(z/21+c, x/20+c)
    ctx.stroke()

def hexagon(c,k1:float, k2:float,k3:float):
    ctx.move_to(0.35+c/10, 0.13+c/10)
    ctx.line_to(0.35+c/10, 0.13+c/10)
    ctx.line_to(0.425+c/10, 0.18+c/10)
    ctx.line_to(0.425+c/10, 0.27+c/10)
    ctx.line_to(0.35+c/10, 0.32+c/10)
    ctx.line_to(0.275+c/10, 0.27+c/10)
    ctx.line_to(0.275+c/10, 0.18+c/10)
    ctx.close_path()

    # ctx.set_source_rgb(1, 0.5, 0)
    # ctx.fill_preserve()

    ctx.set_source_rgb(k1, k2, k3)
    ctx.set_line_width(0.01)
    ctx.stroke()

def circle(x:float,y:float,d:float, k1:float, k2:float,k3:float):
    ctx.set_line_width(0.002)
    ctx.new_sub_path()
    ctx.set_source_rgb(k1, k2, k3)
    ctx.arc(x, y, d, 0, math.pi *2)
    ctx.stroke()



for x in range(12):
    for y in range(12):
        for z in range(1):
            triangle(-x-r/23,y -r/64,-z, r/47, 0.75, 0, 1)
            triangle(x - r / 3, y - r / 6, -z, r / 47, 0.5, 0, 1)
            triangle(-x-r/3,y -r/64,-z, r/47, 0.25, 0.5, 1)
            triangle(x - r / 3, - y - r / 64, z, r / 47, 0.25, 0.25, 1)
            triangle(x - r / 3, - y + r / 64, z, r / 47, 0.25, 0.35, 0.75)
            triangle(x - r / 3, - y + r / 64, - z + r/50, r / 47, 0.25, 0.45, 0.75)



# for x in range(1,2):
#     for y in range(1,2):
#         for d in range(1,2):
#             for c in range(1,2):
#                 circle(x/20-0.02+ c/12, y/1.32 - c/12 -0.2, d/12 - c/60, 0.25,0.5,0.5)
#                 circle(x / 14 +0.4 - c / 35 + r*0.01, y / 1.96 -0.5+ c / 12 + r*0.01, d / 12 - c / 60 + r*0.01)
#                 circle(x/20 + 0.2+ c/12, y/1.32 - c/12 -0.2, d/12 - c/60)
#
# for x in range(1):
#     for y in range(6):
#         for z in range(1):
#             hexagon(x, 1, 1, 1)
#             hexagon(y, 1, 1, 0.5)
#             hexagon(x+ y, 1, 1, 0.25)
#



# ctx.arc(0.0, 0.8, 0.2, -math.pi / 2, 0)
# ctx.line_to(0.5, 0.1)  # Line to (x,y)
# Curve(x1, y1, x2, y2, x3, y3)
# ctx.curve_to(0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
# ctx.close_path()

#ctx.set_source_rgb(1, 1, 1)  # Solid color
#ctx.set_line_width(0.002)
#ctx.stroke()

surface.write_to_png("example22.png")  # Output to PNG
