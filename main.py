import tkinter
import random as r
import time
from tkinter import *
from tkinter import messagebox
import pygame

pygame.mixer.init()


def opening():
    pygame.mixer.music.load("music/obhai.mp3")
    pygame.mixer.music.play(loops=0)
opening()


def fail():
     pygame.mixer.music.load("music/Tada.mp3")
     pygame.mixer.music.play(loops=6)
#fail()

root = Tk()
root.geometry("500x500")
root.minsize(600, 600)
root.maxsize(600, 600)
global pop, b2, b3, extra1


def choice(option):
    if option == "Bat":
        l2 = Label(frame2, text=f"Team Chooses {option}", bg="#f9ca24", font=(
            'calibre', 10, 'bold'))
        l2.place(x=70, y=250)
        b2.destroy()
        b3.destroy()
    else:
        l3 = Label(frame2, text=f"Team Chooses {option}", bg="#f9ca24", font=(
            'calibre', 10, 'bold'))
        l3.place(x=70, y=250)
        b2.destroy()
        b3.destroy()


name_var = StringVar()
passw_var = StringVar()


def toss():
    global b2, b3
    extra1 = name_var.get()
    list2 = ["Tail", "Heads"]
    random_no = r.choice(list2)
    if random_no == "Heads":
        l1 = Label(frame2, text=f"the toss is heads",
                   font=('calibre', 10, 'bold'), bg="#f9ca24")
        l1.place(x=70, y=120)
        sub_btn.destroy()
    else:
        l2 = Label(frame2, text=f"the toss is tails",
                   font=('calibre', 10, 'bold'), bg="#f9ca24")
        l2.place(x=70, y=100)
        sub_btn.destroy()
    if extra1 == random_no:
        l2 = Label(frame2, text=f"{ran} win the toss \n let choose there choice ", font=(
            'calibre', 10, 'bold'), bg="#f9ca24")
        l2.place(x=25, y=200)
        b2 = Button(frame2, text="Ball", bg="#f9ca24", font=(
            'calibre', 10, 'bold'), command=lambda: choice("Ball"))
        b3 = Button(frame2, text="Bat", bg="#f9ca24", font=(
            'calibre', 10, 'bold'), command=lambda: choice("Bat"))
        b2.place(x=90, y=300)
        b3.place(x=130, y=300)
    else:
        l3 = Label(frame2, text=f"{ran} loss the toss \n let other Team choose there choice ", font=(
            'calibre', 10, 'bold'), bg="#f9ca24")
        l3.place(x=25, y=200)
        b2 = Button(frame2, text="Ball", bg="#f9ca24", font=(
            'calibre', 10, 'bold'), command=lambda: choice("Ball"))
        b3 = Button(frame2, text="Bat", bg="#f9ca24", font=(
            'calibre', 10, 'bold'), command=lambda: choice("Bat"))
        b2.place(x=90, y=300)
        b3.place(x=130, y=300)


def submit():
    global ran, name_2
    name_2 = name_var.get()
    list = ["team_1", "team_2"]
    ran = r.choice(list)
    global sub_btn
    name_label = Label(frame2, text=f"{ran} head or tail :", bg="#f9ca24", font=(
        'calibre', 10, 'bold'))
    name_entry = Entry(frame2, textvariable=name_var,
                       font=('calibre', 10, 'normal'))
    sub_btn = Button(frame2, text='Now toss ', bg="#f9ca24", command=toss)
    name_label.place(x=10, y=30)
    name_entry.place(x=10, y=60)
    sub_btn.place(x=10, y=90)


root.configure(bg='black')
frame1 = Frame(root, height=400, width=150, bg="#f9ca24")
frame1.place(x=10, y=10)
mylst = Listbox(frame1, bg="#fff200", height=17)
mylst.place(x=10, y=80)
Label(frame1, text="Enter Team Name", bg="#f9ca24",
      font=('calibre', 10, 'bold')).place(x=10, y=40)
name_var_1 = StringVar()
e5 = Entry(frame1, textvariable=name_var_1, width=20)
e5.place(x=10, y=60)
global Li
li = []
wee = 11


def mydel():
    global wee, j, l3
    if wee != 0:
        j = 0
        name = name_var_1.get()
        mylst.insert(j, f"{wee}-->{name}")
        name_var_1.set("")
        wee = wee - 1
        j = j+1


Button(frame1, text="Add Member", font=('calibre', 10, 'bold'),
       bg="#f9ca24", width=14, command=mydel).place(x=10, y=360)
t1 = Label(frame1, text="Team1", bg="#f9ca24", font=('calibre', 10, 'bold'))
t1.place(x=10, y=10)
frame2 = Frame(root, height=400, width=260, bg="#f9ca24")
frame2.place(x=170, y=10)
submit()
b4 = Label(frame2, text="Selection", bg="#f9ca24",
           font=('calibre', 10, 'bold'))
b4.place(x=10, y=10)
frame3 = Frame(root, height=400, width=150, bg="#f9ca24")
frame3.place(x=440, y=10)
mylst_1 = Listbox(frame3, bg="#fff200", height=17)
mylst_1.place(x=10, y=80)
Label(frame3, text="Enter Team Name", font=(
    'calibre', 10, 'bold'), bg="#f9ca24").place(x=10, y=40)
name_var_2 = StringVar()
e4 = Entry(frame3, textvariable=name_var_2, width=20)
e4.place(x=10, y=60)
we = 11
l1_1 = []


def mydel():
    global we, l2_1
    if we != 0:
        i = 0
        name_1 = name_var_2.get()
        mylst_1.insert(i, f"{we}-->{name_1}")
        name_var_2.set("")
        we = we - 1
        i = i+1


run_team1 = 0
balls_team1 = 12
outcounter = 0
Button(frame3, text="Add Member", font=('calibre', 10, 'bold'),
       bg="#f9ca24", width=14, command=mydel).place(x=10, y=360)
t3 = Label(frame3, text="Team2", font=('calibre', 10, 'bold'), bg="#f9ca24")
t3.place(x=10, y=10)
frame4 = Frame(root, height=170, width=580, bg="#f9ca24")
frame4.place(x=10, y=420)
b6 = Label(frame4, text="Status:", font=('calibre', 10, 'bold'), bg="#f9ca24")
b6.place(x=10, y=10)
summer1 = Button(frame4, text="+1", font=('calibre', 10, 'bold'),
                 bg="#18dcff", command=lambda: sum_team1(1), width=5)
summer1.place(x=20, y=40)
summer2 = Button(frame4, text="+2", font=('calibre', 10, 'bold'),
                 bg="#18dcff", command=lambda: sum_team1(2), width=5)
summer2.place(x=70, y=40)
summer3 = Button(frame4, text="+3", font=('calibre', 10, 'bold'),
                 bg="#18dcff", command=lambda: sum_team1(3), width=5)
summer3.place(x=70, y=70)
summer4 = Button(frame4, text="Four", font=('calibre', 10, 'bold'),
                 bg="#18dcff", command=lambda: sum_team1(4), width=5)
summer4.place(x=120, y=40)
summer5 = Button(frame4, text="Six", font=('calibre', 10, 'bold'),
                 bg="#18dcff", command=lambda: sum_team1(6), width=5)
summer5.place(x=120, y=70)
summer6 = Button(frame4, text="Free", font=('calibre', 10, 'bold'),
                 bg="#18dcff", command=lambda: sum_team1(7), width=5)
summer6.place(x=170, y=40)
outerr = Button(frame4, text="OUT", font=('calibre', 10, 'bold'),
                bg="#18dcff", command=lambda: sum_team1(8), width=5)
outerr.place(x=170, y=70)


def sum_team1(num):
    global run_team1, balls_team1
    if(num == 7):
        run_team1 = run_team1+1
    elif (num == 8):
        global outcounter
        outcounter = outcounter + 1
        balls_team1 = balls_team1 - 1
        if outcounter == 10:
            summer1.destroy()
            summer2.destroy()
            summer3.destroy()
            summer4.destroy()
            summer5.destroy()
            summer6.destroy()
            outerr.destroy()
            run_team2_fun()
        Label(frame4, text="Wickets Lost:", bg="#f9ca24").place(x=130, y=10)
        Label(frame4, text=outcounter, bg="#18dcff").place(x=210, y=10)
        Label(frame4, text=balls_team1, bg="#18dcff").place(x=180, y=140)
        if balls_team1 == 0:
            summer1.destroy()
            summer2.destroy()
            summer3.destroy()
            summer4.destroy()
            summer5.destroy()
            summer6.destroy()
            outerr.destroy()
            run_team2_fun()
        Label(frame4, text="Wickets Lost:", bg="#f9ca24").place(x=130, y=10)
        Label(frame4, text=outcounter, bg="#18dcff").place(x=210, y=10)
        Label(frame4, text=balls_team1, bg="#18dcff").place(x=180, y=140)
    else:
        run_team1 = run_team1+num
        balls_team1 = balls_team1-1
        if balls_team1 == 0:
            summer1.destroy()
            summer2.destroy()
            summer3.destroy()
            summer4.destroy()
            summer5.destroy()
            summer6.destroy()
            outerr.destroy()
            run_team2_fun()
        Label(frame4, text="Wickets Lost:", bg="#f9ca24").place(x=130, y=10)
        Label(frame4, text=outcounter, bg="#18dcff").place(x=210, y=10)
        Label(frame4, text=balls_team1, bg="#18dcff").place(x=180, y=140)
    Label(frame4, text="Runs:", bg="#f9ca24").place(x=10, y=140)
    Label(frame4, text=run_team1, bg="#18dcff").place(x=60, y=140)
    Label(frame4, text="Balls left:", bg="#f9ca24").place(x=120, y=140)
    Label(frame4, text=balls_team1, bg="#18dcff").place(x=180, y=140)


run_team2 = 0
balls_team2 = 12


def run_team2_fun():
    global summer_1, summer_2, summer_3, summer_4, summer_5, summer_6, outerr_1
    b6 = Label(frame4, text="Status_2", bg="#f9ca24")
    b6.place(x=300, y=10)
    summer_1 = Button(frame4, text="+1", bg="#18dcff",
                      command=lambda: sum_team2(1), width=5)
    summer_1.place(x=300, y=40)
    summer_2 = Button(frame4, text="+2", bg="#18dcff",
                      command=lambda: sum_team2(2), width=5)
    summer_2.place(x=350, y=40)
    summer_3 = Button(frame4, text="+3", bg="#18dcff",
                      command=lambda: sum_team2(3), width=5)
    summer_3.place(x=350, y=70)
    summer_4 = Button(frame4, text="Four", bg="#18dcff",
                      command=lambda: sum_team2(4), width=5)
    summer_4.place(x=400, y=40)
    summer_5 = Button(frame4, text="Six", bg="#18dcff",
                      command=lambda: sum_team2(6), width=5)
    summer_5.place(x=400, y=70)
    summer_6 = Button(frame4, text="Free", bg="#18dcff",
                      command=lambda: sum_team2(7), width=5)
    summer_6.place(x=450, y=40)
    outerr_1 = Button(frame4, text="OUT", bg="#18dcff",
                      command=lambda: sum_team2(8), width=5)
    outerr_1.place(x=450, y=70)


outcounter_1 = 0


def sum_team2(num):
    global run_team2, balls_team2
    if(num == 7):
        run_team2 = run_team2+1
    elif(num == 8):
        fail()
        global outcounter_1
        outcounter_1 = outcounter_1 + 1
        balls_team2 = balls_team2-1
        if outcounter_1 == 10:
            summer_1.destroy()
            summer_2.destroy()
            summer_3.destroy()
            summer_4.destroy()
            summer_5.destroy()
            summer_6.destroy()
            outerr_1.destroy()
            check()
        Label(frame4, text="Wickets Lost:", bg="#f9ca24").place(x=450, y=10)
        Label(frame4, text=outcounter_1, bg="#18dcff").place(x=530, y=10)
        Label(frame4, text=balls_team2, bg="#18dcff").place(x=460, y=140)
        if balls_team2 == 0:
            summer_1.destroy()
            summer_2.destroy()
            summer_3.destroy()
            summer_4.destroy()
            summer_5.destroy()
            summer_6.destroy()
            outerr_1.destroy()
            check()
        Label(frame4, text="Wickets Lost:", bg="#f9ca24").place(x=450, y=10)
        Label(frame4, text=outcounter_1, bg="#18dcff").place(x=530, y=10)
        Label(frame4, text=balls_team2, bg="#18dcff").place(x=460, y=140)
    else:
        run_team2 = run_team2 + num
        balls_team2 = balls_team2 - 1
        if balls_team2 == 0:
            summer_1.destroy()
            summer_2.destroy()
            summer_3.destroy()
            summer_4.destroy()
            summer_5.destroy()
            summer_6.destroy()
            outerr_1.destroy()
            check()
    Label(frame4, text="Runs:", bg="#f9ca24").place(x=300, y=140)
    Label(frame4, text=run_team2, bg="#18dcff").place(x=350, y=140)
    Label(frame4, text="Balls left:", bg="#f9ca24").place(x=400, y=140)
    Label(frame4, text=balls_team2, bg="#18dcff").place(x=460, y=140)


def check():
    if run_team1 > run_team2:
        di = run_team1-run_team2
        Label(frame4, text=f" Team_1 is the winner by {di}", bg="#f9ca24").place(
            x=200, y=80)
    if run_team2 > run_team1:
        di = run_team2-run_team1
        Label(frame4, text=f" Team_2 is the winner by {di}", bg="#f9ca24").place(
            x=200, y=80)


# my_canvas=Canvas(frame1,width=1,height=270,fg="Black")
# my_canvas.place(x=8,y=80)
# my_canvas=Canvas(frame1,width=1,height=270,fg="Black")
# my_canvas.place(x=130,y=80)
# my_canvas=Canvas(frame1,width=120,height=1,fg="Black")
# my_canvas.place(x=10,y=78)
# my_canvas=Canvas(frame1,width=123,height=1,fg="Black")
# my_canvas.place(x=8,y=350)
root.title("Cricket")
mainloop()
