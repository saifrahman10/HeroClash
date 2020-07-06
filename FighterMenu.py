import tkinter

from HeroClass import *
from HeroClashGUI import *
from PIL import Image, ImageTk
from FighterProfiles import *
import random

player1, player2, player1ai, player2ai=None,None,False,False

# Function to disable superhero once selected
def disableHero(hero):
    if hero == batman:
        batman_button.configure(state=DISABLED)
    if hero == joker:
        joker_button.configure(state=DISABLED)
    if hero == superman:
        superman_button.configure(state=DISABLED)
    if hero == bane:
        bane_button.configure(state=DISABLED)
    if hero == aquaman:
        aquaman_button.configure(state=DISABLED)
    if hero == darkseid:
        darkseid_button.configure(state=DISABLED)

def displayfight(player):
    player_img = Image.open('Fighters/' + player.name + 'Icon.png')
    player_img = player_img.resize((100, 100), Image.ANTIALIAS)
    player_img_resize = ImageTk.PhotoImage(player_img)
    if player == player1:
        player1display.config(image=player_img_resize)
        player1display.image=player_img_resize
    else:
        player2display.config(image=player_img_resize)
        player2display.image = player_img_resize

# Disables chosen player 1 hero and
def player1disable():
    disableHero(player1)
    choose_var.set('PLAYER 2, CHOOSE YOUR FIGHTER!')

def randombutton(tk):
    global player1, player2
    if player1 == None:
        player1 = random.choice(fighters)
        displayfight(player1)
        p1_text.set(player1.name)
        if player1ai:
            player1.ai=True
        player1disable()
    elif player2 == None:
        player2 = random.choice(fighters)
        displayfight(player2)
        p2_text.set(player2.name)
        if player2ai:
            player2.ai=True

# Function to assign chosen hero to player 1 or 2; if AI for either player 1 or player, choose random.
def buttonClick(tk,hero=None,comp=None,button=None):
    global player1,player2, player1ai, player2ai
    if button:
        if player1 and player2:
            tk.destroy()
        else:
            choose_var.set('PLEASE CHOOSE A FIGHTER!')
    else:
        if player1 == None:
            player1 = hero
            displayfight(player1)
            p1_text.set(hero.name)
            if player1ai:
                player1.ai=True
            player1disable()
        elif player1 != None:
            player2 = hero
            displayfight(player2)
            p2_text.set(hero.name)
            if player2ai:
                player2.ai=True

def player1drop(event):
    global player1, player2, player1ai
    if event == 'CPU':
        if player2 != None or player1==None:
            choose_var.set('PLAYER 1: CHOOSE CPU')
        if player1:
            player1.ai = True
        else:
            player1ai = True
    if event == 'PLAYER 1':
        if player2 != None or player1==None:
            choose_var.set('PlAYER 1: CHOOSE YOUR FIGHTER')
        if player1:
            player1.ai = False
        else:
            player1ai = False

def player2drop(event):
    global player1, player2, player2ai
    if event=='CPU':
        if player1 != None:
            choose_var.set('PLAYER 2: CHOOSE CPU')
        if player2:
            player2.ai=True
        else:
            player2ai=True
    if event=='PLAYER 2':
        if player1 != None:
            choose_var.set('PLAYER 2: CHOOSE YOUR FIGHTER')
        if player2:
            player2.ai=False
        else:
            player2ai=False

# Main display
tk = Tk()
tk.title('Fighter Menu')
tk.geometry('315x430')

choose_var = StringVar()
choose_var.set('PLAYER 1: CHOOSE YOUR FIGHTER')

choose_label = Label(tk, textvariable=choose_var)
choose_label.grid(row=0,column=0, columnspan=3)

# Hero setup
batman_img_resize = ImageTk.PhotoImage(batman_img)
batman_button = Button(tk, image=batman_img_resize, command=lambda: buttonClick(tk, batman))
batman_button.grid(row=1,column=0)

joker_img_resize = ImageTk.PhotoImage(joker_img)
joker_button = Button(tk, image=joker_img_resize, command=lambda: buttonClick(tk, joker))
joker_button.grid(row=1,column=1)

superman_img_resize = ImageTk.PhotoImage(superman_img)
superman_button = Button(tk, image=superman_img_resize, command=lambda: buttonClick(tk, superman))
superman_button.grid(row=1,column=2)

bane_img_resize = ImageTk.PhotoImage(bane_img)
bane_button = Button(tk, image=bane_img_resize, command=lambda: buttonClick(tk, bane))
bane_button.grid(row=2,column=0)

aquaman_img_resize = ImageTk.PhotoImage(aquaman_img)
aquaman_button = Button(tk, image=aquaman_img_resize, command=lambda: buttonClick(tk, aquaman))
aquaman_button.grid(row=2,column=1)

darkseid_img_resize = ImageTk.PhotoImage(darkseid_img)
darkseid_button = Button(tk, image=darkseid_img_resize, command=lambda: buttonClick(tk, darkseid))
darkseid_button.grid(row=2,column=2)

random_button = Button(tk, text='RANDOM', command=lambda: randombutton(tk), state=NORMAL)
random_button.grid(row=5,column=1, columnspan=1)

# Fight Display
gapdisplay = Label(text='')
gapdisplay.grid(row=6,column=0, columnspan=3)

player1_text = StringVar()
player1_text.set('PLAYER 1')
player1_dropdown = OptionMenu(tk, player1_text, 'PLAYER 1', 'CPU',command=player1drop)
player1_dropdown.grid(row=7,column=0)

player2_text = StringVar()
player2_text.set('PLAYER 2')
player2_dropdown = OptionMenu(tk, player2_text, 'PLAYER 2', 'CPU',command=player2drop)
player2_dropdown.grid(row=7,column=2)

fightpreview = Label(text='MATCH')
fightpreview.grid(row=7,column=1)

player1_img = Image.open('Fighters/Question.jpg')
player1_img = player1_img.resize((100,100),Image.ANTIALIAS)
player1_img_resize = ImageTk.PhotoImage(player1_img)
player1display = Label(tk, image=player1_img_resize)
player1display.grid(row=8,column=0)

versus = Label(text='VERSUS')
versus.grid(row=8,column=1)

player2_img = Image.open('Fighters/Question.jpg')
player2_img = player2_img.resize((100,100),Image.ANTIALIAS)
player2_img_resize = ImageTk.PhotoImage(player2_img)
player2display = Label(image=player2_img_resize)
player2display.grid(row=8,column=2)

start_button = Button(tk, text='START MATCH', command=lambda: buttonClick(tk,button=start_button))
start_button.grid(row=9,column=1)

p1_text = StringVar()
p1_label = Label(tk, textvariable=p1_text)
p1_label.grid(row=9,column=0)

p2_text = StringVar()
p2_label = Label(tk, textvariable=p2_text)
p2_label.grid(row=9,column=2)

tk.mainloop()
HeroClashFight(player1,player2)


