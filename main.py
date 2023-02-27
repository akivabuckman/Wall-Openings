from tkinter import *
from tkinter import messagebox, PhotoImage
import tkinter as tk
import turtle as trt
from turtle import setworldcoordinates, TurtleScreen, RawTurtle


def starting_params():
    global ceiling_height
    global section_width
    ceiling_height = ceiling_height_entry.get()
    section_width = section_width_entry.get()
    start_window.destroy()


def home_screen(widgets):
    for i in widgets:
        i.destroy()
    # Labels
    add_label = tk.Label(text="Choose next element:", font=("Calibri (Body)", 22))
    add_label.grid(row=0, column=0, pady=5, padx=5)
    # Buttons
    rectangle_button = tk.Button(master=start_window, image=rectangle_image, bd=0,
                                 command=lambda: get_rectangle_info(widgets))
    rectangle_button.grid(row=1, column=0, padx=5)
    circle_button = tk.Button(master=start_window, image=circle_image, bd=0, command=lambda: get_circle_info(widgets))
    circle_button.grid(row=2, column=0)
    wall_button = tk.Button(master=start_window, image=wall_image, bd=0, command=lambda: get_wall_info(widgets))
    wall_button.grid(row=3, column=0)
    restart_button = tk.Button(image=restart_image, bd=0, command=restart)
    restart_button.grid(row=4, column=0)
    name_label = tk.Label(text="Made by Akiva Buckman", font=("Calibri (Body)", 16))
    name_label.grid(row=30, column=0, columnspan=3)

    widgets = [add_label, rectangle_button, circle_button, wall_button, restart_button]


def initialize():
    global ceiling_height_entry
    global section_width_entry
    global start_window
    start_window = Tk()
    start_window.title("Wall Opening Builder")
    start_window.config(padx=5, pady=5)
    welcome = tk.Label(text="Hey there, let's create a wall")
    welcome.grid(row=0, column=0, columnspan=3)

    # Labels
    section_width_label = tk.Label(text="What's the section's width?")
    section_width_label.grid(row=1, column=0)
    section_width_label_cm = tk.Label(text="[cm]")
    section_width_label_cm.grid(row=1, column=2)
    ceiling_height_label = tk.Label(text="What's the ceiling height?")
    ceiling_height_label.grid(row=2, column=0)
    ceiling_height_label_cm = tk.Label(text="[cm]")
    ceiling_height_label_cm.grid(row=2, column=2)

    # Entries
    section_width_entry = tk.Entry(start_window)
    section_width_entry.grid(row=1, column=1)
    section_width_entry.focus()
    ceiling_height_entry = tk.Entry(start_window)
    ceiling_height_entry.grid(row=2, column=1)

    # Buttons
    submit_button = Button(start_window, text="Let's draw!", command=starting_params)
    submit_button.grid(row=3, column=0, columnspan=3)
    start_window.mainloop()


def restart():
    global ceiling_height
    draw.clear()
    draw.goto(0, 0)
    draw_ceiling_and_floor(ceiling_height)


def draw_ceiling_and_floor(ceiling_height):
    draw.goto(0, ceiling_height * FACTOR)
    draw.pendown()
    draw.seth(0)
    draw.forward(section_width * FACTOR)
    draw.penup()
    draw.goto(0, 0)
    draw.pendown()
    draw.forward(section_width * FACTOR)
    draw.penup()
    draw.goto(0, 0)


def get_rectangle_info(widgets):
    global existing
    existing = True
    for i in widgets:
        i.destroy()

    rec_label = tk.Label(text="New Rectangle Opening:")
    rec_label.grid(row=0, column=1, columnspan=2)

    rec_width_label = tk.Label(text="Width [cm]: ", padx=10)
    rec_height_label = tk.Label(text="Height [cm]:")
    rec_elevation_label = tk.Label(text="Elevation [cm]: ")
    rec_fromlast_label = tk.Label(text="Distance from last [cm]: ", padx=10)
    rec_width_label.grid(row=2, column=1)
    rec_height_label.grid(row=3, column=1)
    rec_elevation_label.grid(row=4, column=1)
    rec_fromlast_label.grid(row=5, column=1)

    w = 15
    rec_width_entry = tk.Entry(width=w)
    rec_width_entry.grid(row=2, column=2, padx=10)
    rec_height_entry = tk.Entry(width=w)
    rec_height_entry.grid(row=3, column=2)
    rec_elevation_entry = tk.Entry(width=w)
    rec_elevation_entry.grid(row=4, column=2)
    rec_fromlast_entry = tk.Entry(width=w)
    rec_fromlast_entry.grid(row=5, column=2)
    rec_width_entry.focus()

    toggle_label = tk.Label(text="Existing")
    toggle_button = tk.Button(image=blue_image, bd=0, command=lambda: get_rectangle_info_green(widgets))
    toggle_label.grid(row=1, column=2, sticky="w")
    toggle_button.grid(row=1, column=1, sticky="e")

    rec_ok_button = tk.Button(image=submit_image, bd=0, command=lambda: draw_rectangle(rec_width_entry.get(),
                                                                                       rec_height_entry.get(),
                                                                                       rec_elevation_entry.get(),
                                                                                       rec_fromlast_entry.get(),
                                                                                       widgets))
    rec_ok_button.grid(row=6, column=1, columnspan=2, rowspan=5)

    rec_cancel_button = tk.Button(image=back_image, bd=0, command=lambda: home_screen(widgets))
    rec_cancel_button.grid(row=0, column=0, padx=5)
    widgets = [rec_label, rec_width_label, rec_height_label, rec_elevation_label, rec_fromlast_label, rec_width_entry,
               rec_height_entry, rec_elevation_entry, rec_fromlast_entry, rec_ok_button, rec_cancel_button,
               toggle_button, toggle_label]


def get_rectangle_info_green(widgets):
    # global toggle_button
    # global toggle_label
    global existing
    existing = False

    for i in widgets:
        i.destroy()

    rec_label = tk.Label(text="New Rectangle Opening:")
    rec_label.grid(row=0, column=1, columnspan=2)

    rec_width_label = tk.Label(text="Width [cm]: ", padx=10)
    rec_height_label = tk.Label(text="Height [cm]:")
    rec_elevation_label = tk.Label(text="Elevation [cm]: ")
    rec_fromlast_label = tk.Label(text="Distance from last [cm]: ", padx=10)
    rec_width_label.grid(row=2, column=1)
    rec_height_label.grid(row=3, column=1)
    rec_elevation_label.grid(row=4, column=1)
    rec_fromlast_label.grid(row=5, column=1)

    w = 15
    rec_width_entry = tk.Entry(width=w)
    rec_width_entry.grid(row=2, column=2, padx=10)
    rec_height_entry = tk.Entry(width=w)
    rec_height_entry.grid(row=3, column=2)
    rec_elevation_entry = tk.Entry(width=w)
    rec_elevation_entry.grid(row=4, column=2)
    rec_fromlast_entry = tk.Entry(width=w)
    rec_fromlast_entry.grid(row=5, column=2)
    rec_width_entry.focus()

    toggle_label = tk.Label(text="New")
    toggle_button = tk.Button(image=green_image, bd=0, command=lambda: get_rectangle_info(widgets))
    toggle_label.grid(row=1, column=2, sticky="w")
    toggle_button.grid(row=1, column=1, sticky="e")

    rec_ok_button = tk.Button(image=submit_image, bd=0, command=lambda: draw_rectangle(rec_width_entry.get(),
                                                                                       rec_height_entry.get(),
                                                                                       rec_elevation_entry.get(),
                                                                                       rec_fromlast_entry.get(),
                                                                                       widgets))
    rec_ok_button.grid(row=6, column=1, columnspan=2, rowspan=5)

    rec_cancel_button = tk.Button(image=back_image, bd=0, command=lambda: home_screen(widgets))
    rec_cancel_button.grid(row=0, column=0, padx=5)
    widgets = [rec_label, rec_width_label, rec_height_label, rec_elevation_label, rec_fromlast_label, rec_width_entry,
               rec_height_entry, rec_elevation_entry, rec_fromlast_entry, rec_ok_button, rec_cancel_button,
               toggle_button,
               toggle_label]


def get_circle_info(widgets):
    for i in widgets:
        i.destroy()
    global existing
    existing = True
    cir_label = tk.Label(text="New Circle Opening:")
    cir_label.grid(row=0, column=1, columnspan=2)

    cir_diameter_label = tk.Label(text="Diameter [cm]: ")
    cir_elevation_label = tk.Label(text="Center's Elevation [cm]: ")
    cir_fromlast_label = tk.Label(text="Distance from last [cm]: ")
    cir_diameter_label.grid(row=2, column=1)
    cir_elevation_label.grid(row=3, column=1)
    cir_fromlast_label.grid(row=4, column=1)

    w = 15
    cir_diameter_entry = tk.Entry(width=w)
    cir_diameter_entry.grid(row=2, column=2, padx=10)
    cir_elevation_entry = tk.Entry(width=w)
    cir_elevation_entry.grid(row=3, column=2)
    cir_fromlast_entry = tk.Entry(width=w)
    cir_fromlast_entry.grid(row=4, column=2)
    cir_diameter_entry.focus()

    toggle_label = tk.Label(text="Existing")
    toggle_button = tk.Button(image=blue_image, bd=0, command=lambda: get_circle_info_green(widgets))
    toggle_label.grid(row=1, column=2, sticky="w")
    toggle_button.grid(row=1, column=1, sticky="e")

    cir_ok_button = tk.Button(image=submit_image, bd=0, command=lambda: draw_circle(cir_diameter_entry.get(),
                                                                                    cir_elevation_entry.get(),
                                                                                    cir_fromlast_entry.get(), widgets))
    cir_ok_button.grid(row=5, column=1, columnspan=2, rowspan=5)

    cir_cancel_button = tk.Button(image=back_image, bd=0, command=lambda: home_screen(widgets))
    cir_cancel_button.grid(row=0, column=0, padx=5)

    widgets = [cir_label, cir_diameter_label, cir_diameter_entry, cir_elevation_entry, cir_elevation_label,
               cir_fromlast_entry, cir_fromlast_label, cir_ok_button, cir_cancel_button, toggle_button, toggle_label]


def get_circle_info_green(widgets):
    for i in widgets:
        i.destroy()
    global existing
    existing = False
    cir_label = tk.Label(text="New Circle Opening:")
    cir_label.grid(row=0, column=1, columnspan=2)

    cir_diameter_label = tk.Label(text="Diameter [cm]: ")
    cir_elevation_label = tk.Label(text="Center's Elevation [cm]: ")
    cir_fromlast_label = tk.Label(text="Distance from last [cm]: ")
    cir_diameter_label.grid(row=2, column=1)
    cir_elevation_label.grid(row=3, column=1)
    cir_fromlast_label.grid(row=4, column=1)

    w = 15
    cir_diameter_entry = tk.Entry(width=w)
    cir_diameter_entry.grid(row=2, column=2, padx=10)
    cir_elevation_entry = tk.Entry(width=w)
    cir_elevation_entry.grid(row=3, column=2)
    cir_fromlast_entry = tk.Entry(width=w)
    cir_fromlast_entry.grid(row=4, column=2)
    cir_diameter_entry.focus()

    toggle_label = tk.Label(text="New")
    toggle_button = tk.Button(image=green_image, bd=0, command=lambda: get_circle_info(widgets))
    toggle_label.grid(row=1, column=2, sticky="w")
    toggle_button.grid(row=1, column=1, sticky="e")

    cir_ok_button = tk.Button(image=submit_image, bd=0, command=lambda: draw_circle(cir_diameter_entry.get(),
                                                                                    cir_elevation_entry.get(),
                                                                                    cir_fromlast_entry.get(), widgets))
    cir_ok_button.grid(row=5, column=1, columnspan=2, rowspan=5)

    cir_cancel_button = tk.Button(image=back_image, bd=0, command=lambda: home_screen(widgets))
    cir_cancel_button.grid(row=0, column=0, padx=5)

    widgets = [cir_label, cir_diameter_label, cir_diameter_entry, cir_elevation_entry, cir_elevation_label,
               cir_fromlast_entry, cir_fromlast_label, cir_ok_button, cir_cancel_button, toggle_button, toggle_label]


def get_wall_info(widgets):
    for i in widgets:
        i.destroy()

    wall_label = tk.Label(text="New Wall:")
    wall_label.grid(row=0, column=1, columnspan=2)

    wall_width_label = tk.Label(text="Width [cm]: ")
    wall_fromlast_label = tk.Label(text="Distance from last [cm]: ")
    wall_width_label.grid(row=1, column=1)
    wall_fromlast_label.grid(row=2, column=1)

    wall_width_entry = tk.Entry()
    wall_width_entry.grid(row=1, column=2, padx=10)
    wall_fromlast_entry = tk.Entry()
    wall_fromlast_entry.grid(row=2, column=2)
    wall_width_entry.focus()

    wall_ok_button = tk.Button(image=submit_image, bd=0, command=lambda: draw_wall(wall_width_entry.get(),
                                                                                   wall_fromlast_entry.get(), widgets))
    wall_ok_button.grid(row=3, column=1, columnspan=2, rowspan=5)

    wall_cancel_button = tk.Button(image=back_image, bd=0, command=lambda: home_screen(widgets))
    wall_cancel_button.grid(row=0, column=0, padx=5)

    widgets = [wall_label, wall_width_label, wall_width_entry, wall_fromlast_entry, wall_fromlast_label, wall_ok_button,
               wall_cancel_button]


def draw_rectangle(width, height, elevation, fromlast, widgets):
    global ELEMENTS
    global measure_height
    global TICK
    global existing
    entries = [width, height, elevation, fromlast]
    errors = ""
    for i in entries:
        try:
            i = int(i)
        except ValueError:
            errors += f"{i}, "
    if len(errors) > 0:
        messagebox.showwarning("Uh oh", f"You entered '{errors}'and all parameters must be numbers.")
        if existing:
            get_rectangle_info(widgets)
        else:
            get_rectangle_info_green(widgets)
        return
    # check for ceiling or floor clash
    if int(elevation) + int(height) > ceiling_height:
        messagebox.showwarning("Watch out!", "Careful - that's hitting the ceiling.")

    if int(elevation) < 0:
        messagebox.showwarning("Watch out!", "Careful - that's hitting the floor.")

    # draw fromlast ticks and measurements
    home_screen(widgets)

    draw.penup()
    draw.seth(90)
    draw.forward(measure_height * FACTOR)
    draw.seth(45)
    draw.pendown()
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.forward(int(fromlast) * FACTOR)
    draw.seth(45)
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.penup()
    draw.back(int(fromlast) * FACTOR / 2)
    draw.seth(90)
    draw.forward(5)
    draw.write(fromlast, font=("Arial", 10, "normal"), align="Center")
    draw.back(5)
    draw.seth(0)
    draw.forward(int(fromlast) * FACTOR / 2)
    draw.setheading(90)
    draw.penup()
    draw.back(measure_height * FACTOR)

    # draw rectangle
    if existing:
        draw.color("Blue")
    else:
        draw.color("Green")
    draw.forward(int(elevation) * FACTOR)
    draw.pendown()
    draw.forward(int(height) * FACTOR)
    draw.right(90)
    draw.forward(int(width) * FACTOR)
    if draw.xcor() > section_width * FACTOR:
        messagebox.showwarning("Careful", "FYI, you're sketching outside the section's width")
    draw.right(90)
    draw.forward(int(height) * FACTOR)
    draw.right(90)
    draw.forward(int(width) * FACTOR)
    draw.right(90)
    draw.penup()
    draw.goto(draw.xcor(), int(elevation) * FACTOR + int(height) * FACTOR / 2)
    draw.color("Black")
    draw.pendown()
    draw.seth(45)
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.forward(int(width) * FACTOR)
    draw.seth(45)
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.penup()
    draw.seth(0)
    draw.back(int(width) * FACTOR / 2)
    draw.seth(90)
    draw.forward(5)
    draw.write(width, font=("Arial", 10, "normal"), align="Center")
    draw.seth(0)
    draw.back(int(width) * FACTOR / 2)
    draw.seth(90)
    draw.goto(draw.xcor(), 0)
    draw.seth(0)
    draw.color("Black")


def draw_circle(diameter, elevation, fromlast, widgets):
    global ELEMENTS
    global measure_height
    global TICK
    global existing

    entries = [diameter, elevation, fromlast]
    errors = ""
    for i in entries:
        try:
            i = int(i)
        except ValueError:
            errors += f"{i} "
    if len(errors) > 0:
        messagebox.showwarning("Uh oh", f"You entered '{errors}', and all parameters must be numbers.")
        if existing:
            get_circle_info(widgets)
        else:
            get_circle_info_green(widgets)
        return
    if int(elevation) + int(diameter) / 2 > ceiling_height:
        messagebox.showwarning("Watch out!", "That's going to hit the ceiling!")
        return
    if int(elevation) - int(diameter) / 2 < 0:
        messagebox.showwarning("Watch out!", "That will hit the floor.")
    home_screen(widgets)

    # draw fromlast and dimension
    draw.seth(90)
    draw.forward(measure_height * FACTOR)
    draw.seth(45)
    draw.pendown()
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.forward(int(fromlast) * FACTOR)
    draw.seth(45)
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.penup()
    draw.back((int(fromlast) * FACTOR / 2))
    draw.seth(90)
    draw.forward(5)
    draw.write(fromlast, font=("Arial", 10, "normal"), align="Center")
    draw.back(5)
    draw.seth(0)

    # draw circle
    if existing:
        draw.color("Blue")
    else:
        draw.color("Green")
    draw.forward(int(fromlast) * FACTOR / 2)
    draw.goto(draw.xcor(), int(elevation) * FACTOR - int(diameter) * FACTOR / 2)
    draw.pendown()
    draw.circle(int(diameter) * FACTOR / 2)
    if draw.xcor() + int(diameter) * FACTOR / 2 > section_width * FACTOR:
        messagebox.showwarning("Careful", "FYI, you're sketching outside the section's width")

    # draw circle dimension
    draw.color("Black")
    draw.penup()
    draw.back(int(diameter) * FACTOR / 2)
    draw.goto(draw.xcor(), int(elevation) * FACTOR)
    draw.seth(45)
    draw.pendown()
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.forward(int(diameter) * FACTOR)
    draw.pendown()
    draw.seth(45)
    draw.pendown()
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.penup()
    draw.back(int(diameter) * FACTOR / 2)
    draw.seth(90)
    draw.forward(5)
    draw.write(diameter, font=("Arial", 10, "normal"), align="Center")
    draw.goto(draw.xcor(), 0)
    draw.seth(0)


def draw_wall(width, fromlast, widgets):
    entries = [width, fromlast]
    errors = ""
    for i in entries:
        try:
            i = int(i)
        except ValueError:
            errors += f"{i} and"
    if len(errors) > 0:
        messagebox.showwarning("Uh oh", f"You entered '{errors}', all parameters must be numbers.")
        get_wall_info()
        return

    home_screen(widgets)
    # draw fromlast ticks and measurements
    draw.penup()
    draw.seth(90)
    draw.forward(measure_height * FACTOR)
    draw.seth(45)
    draw.pendown()
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.forward(int(fromlast) * FACTOR)
    draw.seth(45)
    draw.forward(TICK)
    draw.back(TICK * 2)
    draw.forward(TICK)
    draw.seth(0)
    draw.penup()
    draw.back(int(fromlast) * FACTOR / 2)
    draw.seth(90)
    draw.forward(5)
    draw.write(fromlast, font=("Arial", 10, "normal"), align="Center")
    draw.back(5)
    draw.seth(0)
    draw.forward(int(fromlast) * FACTOR / 2)
    draw.penup()
    draw.goto(draw.xcor(), 0)

    # draw wall
    draw.setheading(90)
    draw.pendown()
    draw.forward(int(ceiling_height) * FACTOR)
    draw.seth(0)
    draw.forward(int(width) * FACTOR)
    draw.seth(270)
    draw.forward(int(ceiling_height) * FACTOR)
    draw.seth(0)
    draw.penup()
    if draw.xcor() > section_width * FACTOR:
        messagebox.showwarning("Careful", "FYI, you're sketching outside the section's width")


# Starting variables:
for i in range(1):
    widgets = []
    existing = True
    window_exists = False
    initialize()
    need_ceiling_height = True
    need_section_width = True
    while not (not need_ceiling_height or not need_section_width):
        try:
            section_width = int(section_width)
        except ValueError:
            try:
                ceiling_height = int(ceiling_height)
            except ValueError:
                messagebox.showwarning("Uh oh!",
                                       f"You entered '{section_width}' and '{ceiling_height}' as the section width and ceiling" \
                                       f" height, and those aren't numbers.")
                initialize()
            else:
                messagebox.showwarning("Uh oh!",
                                       f"You entered '{section_width}' as the section width, and that's not a number.")
                initialize()
        else:
            need_section_width = False
            try:
                ceiling_height = int(ceiling_height)
            except ValueError:
                need_section_width = True
                messagebox.showwarning("Uh oh!",
                                       f"You entered '{ceiling_height}' as the ceiling height, and that's not a number.")
                initialize()
            else:
                need_ceiling_height = False
                measure_height = ceiling_height / 2

# Drawing Space #
for i in range(1):
    start_window = tk.Tk()
    start_window.title("Wall Opening Builder")
    WINDOW_HEIGHT = 600
    FACTOR = WINDOW_HEIGHT / ceiling_height
    canvas = tk.Canvas(master=start_window, width=section_width * FACTOR + 50, height=ceiling_height * FACTOR + 50)
    canvas.grid(row=0, column=3, rowspan=30, columnspan=10)
    screen = TurtleScreen(canvas)
    screen.setworldcoordinates(-50, -50, section_width * FACTOR + 50, ceiling_height * FACTOR + 50)
    draw = RawTurtle(screen)
    draw.penup()
    draw.speed("fastest")
    TICK = 10

# Images
for i in range(1):
    blue_original = PhotoImage(file="blue.png")
    blue_img = blue_original.zoom(1)
    blue_image = blue_img.subsample(8)
    green_original = PhotoImage(file="green.png")
    green_img = green_original.zoom(1)
    green_image = green_img.subsample(8)
    back_original = PhotoImage(file="back.png")
    back_img = back_original.zoom(1)
    back_image = back_img.subsample(10)
    circle_original = PhotoImage(file="circle.png")
    circle_img = circle_original.zoom(1)
    circle_image = circle_img.subsample(1)
    rectangle_original = PhotoImage(file="rectangle.png")
    rectangle_img = rectangle_original.zoom(1)
    rectangle_image = rectangle_img.subsample(1)
    wall_original = PhotoImage(file="wall.png")
    wall_img = wall_original.zoom(12)
    wall_image = wall_img.subsample(17)
    submit_original = PhotoImage(file="submit.png")
    submit_img = submit_original.zoom(2)
    submit_image = submit_img.subsample(3)
    restart_original = PhotoImage(file="restart.png")
    restart_img = restart_original.zoom(1)
    restart_image = restart_img.subsample(2)

home_screen(widgets)

draw_ceiling_and_floor(ceiling_height)

start_window.mainloop()
