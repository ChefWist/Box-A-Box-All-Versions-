from tkinter import *
import random as r
import os
from csv import reader, writer

#Creates window
root = Tk()
root.title("Box A Box!")
root.geometry("500x400")
root.configure(bg="black")

global speed
global inventory
path = "inventory.csv"
try:
    rows = []

    #Creates Rows(Value) and headers(key)
    with open(path, 'r') as file:
        #reads the file
        csvreader = reader(file)
        #reads the header
        header = next(csvreader)
        #reads the rows
        for row in csvreader:
            rows.append(row)
except FileNotFoundError:
    rows = ["0"]
    with open("inventory.csv", 'w', newline='', encoding='utf-8') as file:
        write = writer(file)
        write.writerow(" ")
        write.writerows(rows)

Oinventory = list(rows)
inventory = []
for i in Oinventory:
  inventory.append(i[0])
#inventory = inventory[0]
#print(inventory)

path = "speed.txt"
try:
    with open(path,"r") as file:
        speed = file.read()
except FileNotFoundError:
    speed = 10
    with open(path,'w') as file:
      file.write(str(speed))

speed = int(speed)


#Creates game assets
box = Canvas(root, width=20, height=20, bg="Orange")

left = Button(root,
              text="Left",
              bg="Black",
              fg="White",
              command=lambda: move(0 - speed, 0),
              padx=20,
              pady=10)
right = Button(root,
               text="Right",
               bg="Black",
               fg="White",
               command=lambda: move(speed, 0),
               padx=20,
               pady=10)
up = Button(root,
            text="Up",
            bg="Black",
            fg="White",
            command=lambda: move(0, 0 - speed),
            padx=20,
            pady=10)
down = Button(root,
              text="Down",
              bg="Black",
              fg="White",
              command=lambda: move(0, speed),
              padx=20,
              pady=10)
shop0 = Button(root,
               text="0$ for speed 10",
               bg="Black",
               fg="White",
               padx=20,
               pady=10,
               command=lambda: buy(price=0, set=10, name="0", obj=shop0))
shop1 = Button(root,
               text="5$ for speed 20",
               bg="Black",
               fg="White",
               padx=20,
               pady=10,
               command=lambda: buy(price=5, set=20, name="1", obj=shop1))
shop2 = Button(root,
               text="10$ for speed 40",
               bg="Black",
               fg="White",
               padx=20,
               pady=10,
               command=lambda: buy(price=10, set=40, name="2", obj=shop2))
shop3 = Button(root,
               text="15$ for speed 60",
               bg="Black",
               fg="White",
               padx=20,
               pady=10,
               command=lambda: buy(price=15, set=60, name="3", obj=shop3))
shop4 = Button(root,
               text="20$ for speed 80",
               bg="Black",
               fg="White",
               padx=20,
               pady=10,
               command=lambda: buy(price=20, set=80, name="4", obj=shop4))
shop5 = Button(root,
               text="25$ for speed 100",
               bg="Black",
               fg="White",
               padx=20,
               pady=10,
               command=lambda: buy(price=25, set=100, name="5", obj=shop5))

if "0" in inventory:
  shop0.config(text="set speed to: 10")
  
if "1" in inventory:
  shop1.config(text="set speed to: 20")
  
if "2" in inventory:
  shop2.config(text="set speed to: 40")
  
if "3" in inventory:
  shop3.config(text="set speed to: 60")

if "4" in inventory:
  shop4.config(text="set speed to: 80")

if "5" in inventory:
  shop5.config(text="set speed to: 100")
  
enemy = Canvas(root, width=20, height=20, bg="Red")

global score
path = "score.txt"
try:
    with open(path,"r") as file:
        score = file.read()
except FileNotFoundError:
    score = 0
    with open(path,'w') as file:
      file.write(str(score))
score = int(score)




#Defines functions


#Deletes main menu screen and creates a new screen
def newScreen(txt, callback):
  play.pack_forget()
  shop.pack_forget()
  help.pack_forget()
  exit.pack_forget()
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
  bx = 0
  by = 0
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
    return str(ex) + " " + str(ey)
  else:
    return False


#Move the Box - Game
def move(x, y):
  global bx
  global by
  global ex
  global ey
  global score
  global header
  bx += x
  by += y
  box.place(x=bx, y=by)
  if round(bx) == round(ex) and round(by) == round(ey):
    enemy.place_forget()
    score+=1
    with open("score.txt",'w') as file:
        file.write(str(score))
    title.config(text=score)


def shopLnd():
  shop0.pack()
  shop1.pack()
  shop2.pack()
  shop3.pack()
  shop4.pack()
  shop5.pack()


def buy(price, set, name, obj):
  global score
  global speed
  global inventory

  if name in inventory:
    speed = set
    with open("speed.txt",'w') as file:
      file.write(str(speed))
    left.config(command=lambda: move(0 - speed, 0))
    up.config(command=lambda: move(0, 0 - speed))
    right.config(command=lambda: move(speed, 0))
    down.config(command=lambda: move(0, speed))
    return 1

  if int(score) >= price:
    score-= price
    with open("score.txt",'w') as file:
        file.write(str(score))
    speed = set
    inventory.append(name)
    print(inventory)
    with open("inventory.csv", 'w', newline='', encoding='utf-8') as file:
      write = writer(file)
      write.writerow(" ")
      write.writerows(inventory)
    title.config(text="Shop: " + str(score))
    left.config(command=lambda: move(0 - speed, 0))
    up.config(command=lambda: move(0, 0 - speed))
    right.config(command=lambda: move(speed, 0))
    down.config(command=lambda: move(0, speed))
    obj.config(text="Set speed to: " + str(set))
  else:
    return 0


def Help():
  helpTxt.pack()


def back():
  play.pack()
  shop.pack()
  help.pack()
  exit.pack()
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
  shop2.forget()
  shop3.forget()
  shop4.forget()
  shop5.forget()


#Creates the title(game name)
title = Label(root,
              text="Box A Box!",
              font=("Arial", 25),
              bg="black",
              fg="white",
              compound="top")
title.pack()

#creates play button
play = Button(root,
              text="Play",
              font=("Arial", 18),
              bg="black",
              fg="white",
              compound="top",
              command=lambda: newScreen(score, start))
play.pack()

#Creates shop button
shop = Button(root,
              text="Shop",
              font=("Arial", 18),
              bg="black",
              fg="white",
              compound="center",
              command=lambda: newScreen("Shop: " + str(score), shopLnd))
shop.pack()

#creates help button
help = Button(root,
              text="Help",
              font=("Arial", 18),
              bg="black",
              fg="white",
              compound="bottom",
              command=lambda: newScreen("Help", Help))
help.pack()

#Creates back button
backBtn = Button(root,
                 text="Back",
                 font=("Arial", 18),
                 bg="black",
                 fg="white",
                 compound="top",
                 command=back)
backBtn.pack_forget()

#Creates Help Text
helpTxt = Label(
    root,
    text=
    "First, press play. Then use the 4 keys(up down, left, right) to move around. Move your orange box on top of the red box.",
    font=("Arial", 18),
    bg="black",
    fg="White")
helpTxt.pack_forget()

#Creates exit button
exit = Button(root,
              text="Exit Game",
              font=("Arial", 18),
              bg="black",
              fg="White",
              command=root.destroy)
exit.pack()

#shows window
root.mainloop()
