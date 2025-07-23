from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
loop = 1
session_text = "Focus"
ticks = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global ticks, loop
    window.after_cancel(timer)
    ticks = ""
    title.config(text="Focus", fg=GREEN)
    checks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    loop = 1
    start_button.config(state="normal")

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    start_button.config(state="disabled")
    global loop
    global session_text
    seconds = 0
    if loop == 1 or loop == 3 or loop == 5 or loop == 7:
        seconds = 30
        session_text = "Work"
        title.config(text=session_text, fg=GREEN)
    elif loop == 2 or loop == 4 or loop == 6:
        seconds = 10
        session_text = "Break"
        title.config(text=session_text, fg=PINK)
    elif loop == 8:
        seconds = 20
        session_text = "Break"
        title.config(text=session_text, fg=RED)

    if loop == 8:
        loop = 0

    loop += 1
    count_down(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    global ticks
    global timer
    current_min = math.floor(count / 60)
    current_sec = count % 60
    if current_sec < 10:
        current_sec = str(current_sec)
        current_sec = '0' + current_sec
    if current_min < 10:
        current_min = str(current_min)
        current_min = '0' + current_min
    canvas.itemconfig(timer_text, text=f"{current_min}:{current_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        if loop % 2 == 1:
            ticks += '✔'
            checks.config(text=ticks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Focus Sessions")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text=session_text, fg=GREEN, font=(FONT_NAME, 40, "bold"),bg=YELLOW, pady=5,padx=20)
title.grid(column=2,row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=3, row=3)

checks = Label(text=ticks,fg=GREEN, font=(FONT_NAME, 20, "bold"),bg=YELLOW, pady=5)
checks.grid(column=2, row=4)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(110, 130, text="00:00", fill="white", font=("Michroma", 20, "bold"))
canvas.grid(column=2, row=2)

window.mainloop()