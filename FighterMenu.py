from HeroClass import *
from HeroClashGUI import *
from PIL import Image, ImageTk
from FighterProfiles import *
import random

player1,player2=None,None

def disableHero(hero):
    if hero == batman:
        Batman_button.configure(state=DISABLED)
    if hero == joker:
        Joker_button.configure(state=DISABLED)
    if hero == superman:
        superman_button.configure(state=DISABLED)
    if hero == bane:
        bane_button.configure(state=DISABLED)
    if hero == aquaman:
        aquaman_button.configure(state=DISABLED)
    if hero == darkseid:
        darkseid_button.configure(state=DISABLED)

def buttonClick(tk,hero=None,comp=None):
    global player1,player2,fighters
    if player1 == None and not comp:
        player1 = hero
        disableHero(hero)
        computer_button.configure(state=NORMAL)
        choose_var.set('Player 2, Choose your fighter!')
    elif player1 != None and not comp :
        player2 = hero
        tk.destroy()
    elif comp and player1 == None:
        player1 = random.choice(fighters)
        player1.ai=True
        disableHero(player1)
        choose_var.set('Player 2, Choose your fighter!')
    elif comp and player1 != None:
        player2 = random.choice(fighters)
        player2.ai=True
        tk.destroy()

tk = Tk()
tk.title('Fighter Menu')
tk.geometry('315x415')

choose_var = StringVar()
choose_var.set('Player 1, Choose your fighter!')

choose_label = Label(tk, textvariable=choose_var)
choose_label.grid(row=0,column=0, columnspan=2)

# Batman Setup
Batman_img = Image.open('Fighters/BatmanIcon.png')
Batman_img = Batman_img.resize((100, 100), Image.ANTIALIAS)
Batman_img_resize = ImageTk.PhotoImage(Batman_img)
Batman_button = Button(tk, image=Batman_img_resize, command=lambda: buttonClick(tk, batman))
Batman_button.grid(row=1,column=0)

joker_img = Image.open('Fighters/JokerIcon.png')
joker_img = joker_img.resize((100,100),Image.ANTIALIAS)
joker_img_resize = ImageTk.PhotoImage(joker_img)
Joker_button = Button(tk, image=joker_img_resize, command=lambda: buttonClick(tk, joker))
Joker_button.grid(row=1,column=1)

superman_img = Image.open('Fighters/SupermanIcon.png')
superman_img = superman_img.resize((100,100),Image.ANTIALIAS)
superman_img_resize = ImageTk.PhotoImage(superman_img)
superman_button = Button(tk, image=superman_img_resize, command=lambda: buttonClick(tk, superman))
superman_button.grid(row=1,column=2)

bane_img = Image.open('Fighters/BaneIcon.png')
bane_img = bane_img.resize((100,100),Image.ANTIALIAS)
bane_img_resize = ImageTk.PhotoImage(bane_img)
bane_button = Button(tk, image=bane_img_resize, command=lambda: buttonClick(tk, bane))
bane_button.grid(row=2,column=0)

aquaman_img = Image.open('Fighters/AquamanIcon.png')
aquaman_img = aquaman_img.resize((100,100),Image.ANTIALIAS)
aquaman_img_resize = ImageTk.PhotoImage(aquaman_img)
aquaman_button = Button(tk, image=aquaman_img_resize, command=lambda: buttonClick(tk, aquaman))
aquaman_button.grid(row=2,column=1)

darkseid_img = Image.open('Fighters/DarkseidIcon.png')
darkseid_img = darkseid_img.resize((100,100),Image.ANTIALIAS)
darkseid_img_resize = ImageTk.PhotoImage(darkseid_img)
darkseid_button = Button(tk, image=darkseid_img_resize, command=lambda: buttonClick(tk, darkseid))
darkseid_button.grid(row=2,column=2)


# Computer Setup
computer_button = Button(tk, text='CPU', command=lambda: buttonClick(tk, comp=True), state=NORMAL)
computer_button.grid(row=5,column=0, columnspan=3)

tk.mainloop()
HeroClashFight(player1,player2)


