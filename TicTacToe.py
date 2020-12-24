#!/usr/bin/env python
# coding: utf-8

# In[4]:


square = [0,1,2,3,4,5,6,7,8,9]

def main():
    player = 1
    status = -1

    while status== -1:
        board()                                # Draw the board on the screen
        
        if player%2 == 1:                      # Find the which player is playing
            player = 1
        else:
            player = 2

        print('\nPlayer', player)              #Print player
        choice = int(input('Enter a number:'))  #Ask the player to enter the choice

        if player == 1:
            mark = 'X'                         #Select mark = X for player 1 and mark = O for player 2
        else:
            mark = 'O'

        if choice == 1 and square[1] == 1:         #check the choice & each square not entered with mark
            square[1] = mark                       # fill the square with mark
        elif choice == 2 and square[2] == 2:
            square[2] = mark
        elif choice == 3 and square[3] == 3:
            square[3] = mark
        elif choice == 4 and square[4] == 4:
            square[4] = mark
        elif choice == 5 and square[5] == 5:
            square[5] = mark
        elif choice == 6 and square[6] == 6:
            square[6] = mark
        elif choice == 7 and square[7] == 7:
            square[7] = mark
        elif choice == 8 and square[8] == 8:
            square[8] = mark
        elif choice == 9 and square[9] == 9:
            square[9] = mark
        else:
            print('Invalid move ')
            player -= 1
                
        status = game_status()              #Check the game status , complete or draw
        player += 1
            
    print('RESULT')    
    if status == 1:
        print('Player',player-1,'win')
    else:
        print('Game draw')
        
        
###############################################
#    FUNCTION TO RETURN GAME STATUS
#    1 FOR GAME IS OVER WITH RESULT
#    -1 FOR GAME IS IN PROGRESS
#    0 GAME IS OVER AND NO RESULT
###############################################

def game_status():
    if square[1] == square[2] and square[2] == square[3]:                  #Compare the single row,column, diagonal 
        return 1                                                           #If all marked the same return 1
    elif square[4] == square[5] and square[5] == square[6]:
        return 1
    elif square[7] == square[8] and square[8] == square[9]:
        return 1
    elif square[1] == square[4] and square[4] == square[7]:
        return 1
    elif square[2] == square[5] and square[5] == square[8]:
        return 1
    elif square[3] == square[6] and square[6] == square[9]:
        return 1
    elif square[1] == square[5] and square[5] == square[9]:
        return 1
    elif square[3] == square[5] and square[5] == square[7]:
        return 1
    elif square[1] != 1 and square[2] != 2 and square[3] != 3 and square[4] != 4 and square[5] != 5 and square[6] != 6 and square[7] != 7 and square[8] != 8 and square[9] != 9:
        return 0
    else:
        return -1
    
    
###############################################
#    FUNCTION TO DRAW BOARD
#    OF TIC TAC TOE WITH PLAYERS MARK
###############################################

def board():
    print('\n\n\tTic Tac Toe\n\n')

    print('Player 1 (X)  -  Player 2 (O)' ) 
    print()

    print('     |     |     ' )
    print(' ' ,square[1] ,' | ' ,square[2] ,' |  ' ,square[3] )

    print('_____|_____|_____' )
    print('     |     |     ' )

    print(' ' ,square[4] ,' | ' ,square[5] ,' |  ' ,square[6] )

    print('_____|_____|_____' )
    print('     |     |     ' )

    print(' ' ,square[7] ,' | ' ,square[8] ,' |  ' ,square[9] )

    print('     |     |     ' )


# In[ ]:


main()
import os    
import time    
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    #Initially Board content are empty
player = 1    
   
###  Flages Used to indicate the status
Win = 1    
Draw = -1    
Running = 0    
Stop = 1    
###########################    
Game = Running                              #Initial Staus of the Game 
Mark = 'X'                                  # Initial Status of the Mark - used to indicate X or O or O
   
#This Function Draws Game Board    
def DrawBoard():                            
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
   
#This Function Checks position is empty or not    
def CheckPosition(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   
#This Function Checks player has won or not    
def CheckWin():    
    global Game    
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win 
        
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
        
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
        
    #Match Tie or Draw Condition    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
print("Player 1 [X] --- Player 2 [O]\n")    
print()    
print()    
print("Please Wait...")    
time.sleep(3)    

while(Game == Running):    
    os.system('cls')    
    DrawBoard()    
    if(player % 2 != 0):    
        print("Player 1's chance")    
        Mark = 'X'    
    else:    
        print("Player 2's chance")    
        Mark = 'O'    
    choice = int(input("Enter the position between [1-9] where you want to mark : "))    
    if(CheckPosition(choice)):              #If True indiicate the position is not selected before
        board[choice] = Mark                #Mark that position
        player+=1                           #Incrment the Player - Next player chance
        CheckWin()                          ##Check the winning condition - will return 'Running' or 'Draw'
    
os.system('cls')    
DrawBoard()    
if(Game==Draw):                        #Display which player won or Draw
    print("Game Draw")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Player 1 Won")    
    else:    
        print("Player 2 Won")  


# In[ ]:




