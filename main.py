from tkinter import * 
import random as r

#Creates window
root = Tk()
root.title("Box A Box!")
root.geometry("500x300")
root.configure(bg = "black")

global speed
global inventory
inventory = []
speed = 10


#Creates game assets
box = Canvas(root, width=20, height=20, bg="Orange")

left = Button(root, text="Left", bg="Black", fg="White", command=lambda: move(0-speed, 0), padx=20, pady=10)
right = Button(root, text="Right", bg="Black", fg="White", command=lambda: move(speed, 0), padx=20, pady=10)
up = Button(root, text="Up", bg="Black", fg="White", command=lambda: move(0, 0-speed), padx=20, pady=10)
down = Button(root, text="Down", bg="Black", fg="White", command=lambda: move(0, speed), padx=20, pady=10)
shop0 = Button(root, text="0$ for speed 10", bg="Black", fg="White", padx=20, pady=10, command=lambda: buy(price=0, set=10, name="S2", obj=shop0))
shop1 = Button(root, text="5$ for speed 20", bg="Black", fg="White", padx=20, pady=10, command=lambda: buy(price=5, set=20, name="S1", obj=shop1))

enemy = Canvas(root, width=20, height=20, bg="Red")

global score 
score = 0



#Defines functions

#Deletes main menu screen and creates a new screen
def newScreen(txt, callback):
  play.pack_forget()
  shop.pack_forget()
  help.pack_forget()
  title.config(text=txt)
  backBtn.pack()
  callback()

#game
def start():
  global bx
  global by 
  read = False
  while read == False:
      read = findRand()
  ex = read.split(sep=" ")[0]
  ey = read.split(sep=" ")[1]
  bx = 240
  by = 140
  box.place(x=bx, y=by)
  left.pack(side=LEFT)
  right.pack(side=RIGHT)
  up.pack(side=TOP)
  down.pack(side=BOTTOM)
  enemy.place(x=ex, y=ey)

def findRand():
  global ex 
  global ey
  global speed
  ex = r.randint(0, 480)
  ey = r.randint(0, 280)
  if ex % speed == 0 and ey % speed == 0:
     return str(ex)+" "+str(ey)
  else:
    return False
 

#Move the Box - Game
def move(x, y):
  global bx
  global by
  global ex 
  global ey
  global score
  bx+=x 
  by+=y
  box.place(x=bx, y=by)
  if round(bx) == round(ex) and round(by) == round(ey):
    enemy.place_forget()
    score+=1
    title.config(text=score)
    
  
  

def shopLnd():
  shop0.pack()
  shop1.pack()

def buy(price, set, name, obj):
  global score
  global speed
  global inventory

  if name in inventory:
    speed = set
    left.config(command=lambda: move(0-speed, 0))
    up.config(command=lambda: move(0, 0-speed))
    right.config(command=lambda: move(speed, 0))
    down.config(command=lambda: move(0, speed))
    return 1

  if score >= price:
    score-=price
    speed = set
    inventory.append(name)
    title.config(text="Shop: "+str(score))
    left.config(command=lambda: move(0-speed, 0))
    up.config(command=lambda: move(0, 0-speed))
    right.config(command=lambda: move(speed, 0))
    down.config(command=lambda: move(0, speed))
    obj.config(text="Set speed to: "+str(set))
  else:
    return 0

def Help():
  helpTxt.pack()

def back():
  play.pack()
  shop.pack()
  help.pack()
  title.config(text="Box A Box!")
  backBtn.pack_forget()
  helpTxt.pack_forget()
  box.place_forget()
  left.forget()
  right.forget()
  up.forget()
  down.forget()
  enemy.place_forget()
  shop0.forget()
  shop1.forget()
  

#Creates the title(game name)
title = Label(root, text="Box A Box!", font=("Arial", 25), bg="black", fg="white", compound="top")
title.pack()

#creates play button
play = Button(root, text="Play", font=("Arial", 18), bg="black", fg="white", compound="top", command=lambda: newScreen(score, start))
play.pack()

#Creates shop button
shop = Button(root, text="Shop", font=("Arial", 18), bg="black", fg="white", compound="center", command=lambda: newScreen("Shop: "+str(score), shopLnd))
shop.pack()

#creates help button
help = Button(root, text="Help", font=("Arial", 18), bg="black", fg="white", compound="bottom", command=lambda: newScreen("Help",Help))
help.pack()

#Creates back button
backBtn = Button(root, text="Back", font=("Arial", 18), bg="black", fg="white", compound="top", command=back)
backBtn.pack_forget()

#Creates Help Text
helpTxt = Label(root, text="press the buttons and move around", font=("Arial",18), bg="black", fg="White")
helpTxt.pack_forget()

#shows window
root.mainloop()