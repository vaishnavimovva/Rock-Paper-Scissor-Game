from tkinter import *
from PIL import Image, ImageTk
from random import randint

# main window
root = Tk()  #main window/widjet
root.title("Rock Paper Scissors") #change title
root.configure(background="DarkOrchid1") #change bg

# picture
rock_img = ImageTk.PhotoImage(Image.open("resources/rockleft.png"))
paper_img = ImageTk.PhotoImage(Image.open("resources/paperleft.png"))
scissor_img = ImageTk.PhotoImage(Image.open("resources/scissorsleft.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("resources/rock.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("resources/paper.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("resources/scissors.png"))

# insert picture
user_label = Label(root, image=rock_img, bg="DarkOrchid1")
comp_label = Label(root, image=rock_img_comp, bg="DarkOrchid1")
comp_label.grid(row=1, column=0)
user_label.grid(row=1, column=9)

# scores
playerScore = Label(root, text= 0, font=1000, bg="DarkOrchid1")
computerScore = Label(root, text= 0, font=1000, bg="DarkOrchid1")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

# headings(user/comp)
user_indicator = Label(root, font=500, text="USER", bg="DarkOrchid1",fg="white")
comp_indicator = Label(root, font=500, text="COMPUTER",bg="DarkOrchid1",fg="white")
user_indicator.grid(row=0, column=3)
comp_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font =100, bg="DarkOrchid1" )
msg.grid(row=1, column=2)

# update message
def updateMessage(x):
    msg['text'] = x

# update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

# update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

# check winner(main gameplay)
def checkWin(player, computer):
    if (computer == 'rock' and player == 'scissor') or (computer == 'paper' and player == 'rock') or (
            computer == 'scissor' and player == 'paper'):
        updateMessage("YOU LOSE!")
        updateCompScore()
    elif (computer == 'rock' and player == 'paper') or (computer == 'paper' and player == 'scissor') or (
            computer == 'scissor' and player == 'rock'):
        updateMessage("YOU WIN!")
        updateUserScore()
    else:
        updateMessage("ITS A TIE!")


# update images according to buttons
choices = ["rock", "paper", "scissor"]


def updateChoice(x):

    # for computer
    compChoice = choices[randint(0, 2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


# for user
    if x == "rock":
        user_label.configure(image=rock_img)
    elif x == "paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)

    checkWin(x, compChoice)


# buttons
rock = Button(root, width=20, height=2, text="ROCK",bg="#E93B6C",command=lambda: updateChoice("rock")).grid(row=2, column=1)
paper = Button(root, width=20, height=2, text="PAPER",bg="yellow",command=lambda: updateChoice("paper")).grid(row=2, column=2)
scissor = Button(root, width=20, height=2, text="SCISSOR",bg="#73d9e1", command=lambda: updateChoice("scissor")).grid(row=2, column=3)
space=Label(root,text=" ",bg="DarkOrchid1").grid(row=3,column=2)
exit = Button(root,width=20, height=2, text="EXIT",bg="black",fg="white",command=root.destroy).grid(row=4, column=2)

#put the entire thing in loop to follow the cursor
root.attributes('-fullscreen',True)
root.mainloop()
