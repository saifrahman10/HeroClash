import time
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import random

# Function to create main window
def HeroClashFight(hero1,hero2):
    tk = Tk()
    tk.geometry('435x510')
    tk.title(hero1.name + ' vs ' + hero2.name)
    hero1.setEnemy(hero2), hero2.setEnemy(hero1)

    # Disable Hero 1 Moves during Hero 2 turn
    def hero1disabled():
        for button in hero1buttons:
            button.configure(state=DISABLED)

    # Disable and Enable moves functions
    def hero2disabled():
        for button in hero2buttons:
            button.configure(state=DISABLED)

    def hero1enabled():
        for button in hero1buttons:
            button.configure(state=NORMAL)

    def hero2enabled():
        for button in hero2buttons:
            button.configure(state=NORMAL)

    # Check which disable/enables are required
    def changebuttonstates(hero):
        if hero1.ai and hero2.ai:
            hero1disabled(), hero2disabled()
        elif hero1.ai:
            hero1disabled(), hero2enabled()
        elif hero2.ai:
            hero2disabled(), hero1enabled()
        elif hero == hero1:
            hero1disabled(), hero2enabled()
        elif hero == hero2:
            hero2disabled(), hero1enabled()

    def ai_move():
        if hero1.ai == True:
            buttonClick(random.choice(hero1buttons), hero1)
        if hero2.ai == True:
            buttonClick(random.choice(hero2buttons), hero2)

    def herohealthUpdate(hero):
        if hero == hero1:
            hero2_health['value'] = hero2.health
        elif hero == hero2:
            hero1_health['value'] = hero1.health

    # Resets fight for next round
    def fightReset():
        hero1.health, hero2.health = 100,100
        hero1_health['value'], hero2_health['value'] = 100,100

    def buttonClick(buttons, hero):
        miss=False
        if buttons['text'] == 'None':
            miss=True
        if buttons['text'] != 'None':
            move_name = buttons['text'].split(':')[0]
            prob = hero.power[move_name][1]
            miss = random.choices([1,0], weights=[prob,1-prob])[0] == 0
        if buttons['text'] != 'None' and not miss:
            hero.attack(buttons['text'].split(':')[0])
            currentturn_text.set(hero.name + ' used ' + buttons['text'].split(':')[0] + '! ' + hero.enemy.name + '\'s turn!')
            herohealthUpdate(hero)
            if hero.enemy.health > 0: # Regular attack, enemy still alive
                if hero.enemy.ai == True:
                    ai_move()
            elif hero.enemy.health <= 0: # Enemy defeated
                hero.wins += 1
                # Check if the hero has 2 wins, if so, game over.
                if hero.wins == 2:
                    if hero == hero1:
                        hero1toptext.set('Wins: 2')
                        hero2_health['value'] = hero2.health
                    elif hero == hero2:
                        hero2toptext.set('Wins: 2')
                    hero1disabled(), hero2disabled()
                    fight_text.set('Game Over\n' + hero.name + ' Wins!')
                    fight_label.configure(fg=hero.color)
                elif hero.wins != 2:
                    fight_text.set('Round ' + str(hero.wins + hero.enemy.wins + 1) + '\nFight!')
                    if hero == hero1:
                        hero1toptext.set('Wins: 1')
                    elif hero == hero2:
                        hero2toptext.set('Wins: 1')
                    time.sleep(1) # Delay for each round
                    fightReset()
        if miss:
            currentturn_text.set(hero.name + ' missed! ' + hero.enemy.name + '\'s turn!')
            if hero.enemy.ai == True:
                ai_move()
        if hero.wins != 2:
            changebuttonstates(hero)

    # Labels each button according to hero moves.
    def label_moves(movebuttons, hero):
        moves = list(hero.power.keys())
        for i in range(len(moves)):
            movebuttons[i].set(moves[i] + ': Damage ' + str(hero.power[moves[i]][0]))

    # Game Detail Labels
    fight_text = StringVar()
    fight_text.set('Round 1\nFight!')
    fight_label = Label(tk, textvariable=fight_text, fg='orange')
    fight_label.grid(row=0, column=1)

    hero1toptext = StringVar()
    hero1toptext.set('Wins: 0')
    hero1toplabel = Label(tk, textvariable=hero1toptext, fg=hero1.color)
    hero1toplabel.grid(row=0,column=0)

    hero2toptext = StringVar()
    hero2toptext.set('Wins: 0')
    hero2toplabel = Label(tk, textvariable=hero2toptext, fg=hero2.color)
    hero2toplabel.grid(row=0,column=2)

    currentturn_text = StringVar()
    currentturn_text.set(hero1.name + '\'s Turn ')
    currentturn = Label(tk, textvariable=currentturn_text)
    currentturn.grid(row=1,column=0,columnspan=3)
    # Hero Labels

    # Image for hero 1
    Hero1_img = Image.open('Fighters/' + hero1.name + '.png')
    Hero1_img = Hero1_img.resize((125,200),Image.ANTIALIAS)
    Hero1_img_resize = ImageTk.PhotoImage(Hero1_img)
    Hero1_img_label = Label(image=Hero1_img_resize)
    Hero1_img_label.grid(row=2,column=0)

    # Label for hero 1 name
    Hero1_Label = Label(text=hero1.name, fg=hero1.color, height=2, width=20)
    Hero1_Label.grid(row=3,column=0)

    # Gap between hero 1 and hero 2
    Gap_Label = Label(height=4, width=5)
    Gap_Label.grid(row=2,column=1,rowspan=5)

    # Image for hero 2
    Hero2_img = Image.open('Fighters/' + hero2.name + '.png')
    Hero2_img = Hero2_img.resize((125,200),Image.ANTIALIAS)
    Hero2_img_resize = ImageTk.PhotoImage(Hero2_img)
    Hero2_img_label = Label(image=Hero2_img_resize)
    Hero2_img_label.grid(row=2,column=2)

    # Label for hero 2 name
    Hero2_Label = Label(text=hero2.name, fg=hero2.color, height=2, width=20)
    Hero2_Label.grid(row=3,column=2)

    # Hero Health Bars
    hero1_health = Progressbar(tk, orient=HORIZONTAL, length=100, mode='determinate')
    hero1_health.grid(row=4,column=0)
    hero1_health['value'] = 100

    hero2_health = Progressbar(tk, orient=HORIZONTAL, length=100, mode='determinate')
    hero2_health.grid(row=4,column=2)
    hero2_health['value'] = 100

    # Move Labels
    move1_label = Label(text='MOVES', height=2, width=20).grid(row=5,column=0)
    move2_label = Label(text='MOVES', height=2, width=20).grid(row=5, column=2)

    # Initialize hero 1 button labels
    hero1mv1,hero1mv2,hero1mv3,hero1mv4=StringVar(),StringVar(),StringVar(),StringVar()
    hero1mv1.set('None'), hero1mv2.set('None'), hero1mv3.set('None'), hero1mv4.set('None')

    # Label hero 1 move buttons
    label_moves([hero1mv1,hero1mv2,hero1mv3,hero1mv4], hero1)

    # Buttons for hero 1 moves, corresponding to button labels above
    hero1_mvbutton1 = Button(tk, textvariable=hero1mv1, height=2, width=20, command=lambda: buttonClick(hero1_mvbutton1, hero1))
    hero1_mvbutton1.grid(row=6,column=0)
    hero1_mvbutton2 = Button(tk, textvariable=hero1mv2, height=2, width=20, command=lambda: buttonClick(hero1_mvbutton2, hero1))
    hero1_mvbutton2.grid(row=7,column=0)
    hero1_mvbutton3 = Button(tk, textvariable=hero1mv3, height=2, width=20, command=lambda: buttonClick(hero1_mvbutton3, hero1))
    hero1_mvbutton3.grid(row=8,column=0)
    hero1_mvbutton4 = Button(tk, textvariable=hero1mv4, height=2, width=20, command=lambda: buttonClick(hero1_mvbutton4, hero1))
    hero1_mvbutton4.grid(row=9,column=0)

    # Initialize hero 2 button labels
    hero2mv1,hero2mv2,hero2mv3,hero2mv4=StringVar(),StringVar(),StringVar(),StringVar()
    hero2mv1.set('None'), hero2mv2.set('None'), hero2mv3.set('None'), hero2mv4.set('None')

    # Label hero 2 move buttons
    label_moves([hero2mv1,hero2mv2,hero2mv3,hero2mv4], hero2)

    # Buttons for hero 2 moves, corresponding to button labels above
    hero2_mvbutton1 = Button(tk, textvariable=hero2mv1, height=2, width=20, command=lambda: buttonClick(hero2_mvbutton1, hero2))
    hero2_mvbutton1.grid(row=6,column=2)
    hero2_mvbutton2 = Button(tk, textvariable=hero2mv2, height=2, width=20, command=lambda: buttonClick(hero2_mvbutton2, hero2))
    hero2_mvbutton2.grid(row=7,column=2)
    hero2_mvbutton3 = Button(tk, textvariable=hero2mv3, height=2, width=20, command=lambda: buttonClick(hero2_mvbutton3, hero2))
    hero2_mvbutton3.grid(row=8,column=2)
    hero2_mvbutton4 = Button(tk, textvariable=hero2mv4, height=2, width=20, command=lambda: buttonClick(hero2_mvbutton4, hero2))
    hero2_mvbutton4.grid(row=9,column=2)

    # Hero Button Lists
    hero1buttons = [hero1_mvbutton1, hero1_mvbutton2, hero1_mvbutton3, hero1_mvbutton4]
    hero2buttons = [hero2_mvbutton1, hero2_mvbutton2, hero2_mvbutton3, hero2_mvbutton4]

    # Round 1 begins with hero 1's turn
    if hero1.ai:
        ai_move()
    elif hero2.ai or (not hero1.ai and not hero2.ai):
        hero2disabled()
    tk.mainloop()