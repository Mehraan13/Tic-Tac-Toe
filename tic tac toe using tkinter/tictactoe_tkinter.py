from tkinter import *
import random

def next_turn(row, column):

    global player
    #   if button is empty and no one has won yet
    if buttons[row][column]['text'] == '' and check_winner() is False:
        
        if player == players[0]: #first players turn
            
            buttons[row][column]['text'] = player 
            #check if this is winning move
            if check_winner() is False:
                #switch players
                player = players[1]
                label.config(text= f'{player} turn')
            #if there is winner
            elif check_winner() is True:
                label.config(text= f'{players[0]} has won!')
            
            elif check_winner() == 'Tie':
                label.config(text='TIE!')

        else: # player 2 turn

            buttons[row][column]['text'] = player 
            #check if this is winning move
            if check_winner() is False:
                #switch players
                player = players[0]
                label.config(text= f'{player} turn')
            #if there is winner
            elif check_winner() is True:
                label.config(text= f'{players[1]} has won!')
            
            elif check_winner() == 'Tie':
                label.config(text='TIE!')

def check_winner():
    #check if along row there is win
    # !! don't forget to put != '' as at the start all buttons are equal to ''
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            buttons[row][0].config(bg = 'green')
            buttons[row][1].config(bg = 'green')
            buttons[row][2].config(bg = 'green')
            
    #check if along column there is win
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != '':
            buttons[0][column].config(bg = 'green')
            buttons[1][column].config(bg = 'green')
            buttons[2][column].config(bg = 'green')
            return True
    #check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        buttons[0][0].config(bg = 'green')
        buttons[1][1].config(bg = 'green')
        buttons[2][2].config(bg = 'green')
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !='':
        buttons[0][2].config(bg = 'green')
        buttons[1][1].config(bg = 'green')
        buttons[2][0].config(bg = 'green')
        return True
    
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg = 'yellow')
        return "Tie"
    
    else:
        return False # no winner no tie

def empty_spaces():
    spaces = 9
    #check all buttons and see if they are empty 
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != '':
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player

    player = random.choice(players)

    label.config(text= f'{player} turn')

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text = '', bg = '#F0F0F0')

# main body 
window = Tk() #create window
window.title('Tic-Tac-Toe') #set title on window

players = ["x","o"] #define players
player = random.choice(players) #choose one random player

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]] #we need buttons 3x3 grid

label = Label(text= player + ' turn', font=('Georgia', 40))
label.pack(side= 'top') #add label to window

reset_button = Button(text='Restart', font = ('consolas',20), command=new_game)
# ^^ place a button to reset the game and this button calls the new_game function
reset_button.pack(side='top')

#create a frame to put the buttons (grid)
frame = Frame(window)
frame.pack()

#take 2d- list and put in frame
for row in range(3):
    for column in range(3):
        #for each place design a button
        #this button command is a lamda function that takes row and column as the arguments and the function next_turn is called
        buttons[row][column] = Button(frame, text='',font=('Georgia', 40), width = 5, height = 2,
                                      command= lambda row= row, column =column: next_turn(row,column))
        #add this button to frame using the grid fucntion
        buttons[row][column].grid(row = row, column = column)


window.mainloop()