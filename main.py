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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60

    if count_sec==0:
        count_sec=int("00")
    if count_sec<10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count>0:
        window.after(1000,count_down,count-1)

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)


title_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"bold"),highlightthickness=0)
title_label.grid(column=1,row=0)
start_label=Button(text="Start",font=(FONT_NAME,10),bg=YELLOW,command=start_timer)
start_label.grid(column=0,row=2)
reset_label=Button(text="Reset",font=(FONT_NAME,10),bg=YELLOW)
reset_label.grid(column=2,row=2)
checkmark_label=Label(text="✅",font=(FONT_NAME,10),highlightthickness=0,fg=GREEN,borderwidth=0,bg=YELLOW)
checkmark_label.grid(column=1,row=3)
window.mainloop()