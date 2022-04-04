#!/usr/bin/env python
# coding: utf-8

# # PROJECT -1

# ## _TIC-TAC-TOE!!!!_
# 

# In[1]:


from IPython.display import clear_output
clear_output()


# In[2]:


#display

def display():
    for x in lis:
        for y in x:
            print(str(y) +"|",end="")
        print("\n")

    


# In[3]:


def check(mark):
    return ((lis[0][0] == mark and lis[0][1] == mark and lis[0][2] == mark) or # across the top
    (lis[1][0] == mark and lis[1][1] == mark and lis[1][2] == mark) or # across the middle
    (lis[2][0] == mark and lis[2][1] == mark and lis[2][2] == mark) or # across the bottom
    (lis[0][0] == mark and lis[1][0] == mark and lis[2][0] == mark) or # down the left side
    (lis[0][1] == mark and lis[1][1] == mark and lis[2][1] == mark) or # down the middle
    (lis[0][2] == mark and lis[1][2] == mark and lis[2][2] == mark) or # down the right side
    (lis[0][0] == mark and lis[1][1] == mark and lis[2][2] == mark) or # right diagonal
    (lis[0][2] == mark and lis[1][1] == mark and lis[2][0] == mark)) # left diagonal
    
    


# In[4]:


def isValid(row,column):
    
    if (row in range(0,3) and column in range(0,3)):
        if (lis[row][column]=="___"):
            return True
        else:
            return False
    else:
        return False


# In[5]:


def place_mark(mark):
    
    while True:    #looping until player gives a valid positon
        pos=list(map(int, input().split()))                  #taking input for position
        if len(pos)==2:
            if isValid(pos[0],pos[1])==False:
                clear_output()
                print("Please enter a valid position")
                display()
            if (isValid(pos[0],pos[1])==True):
                lis[pos[0]][pos[1]]=mark #marking the position in the list
                break
        else:
            print("Please Enter a valid position")
            display()
    return


# In[6]:


def gameplay():
    
    mark=" X "
    game_status="ON"

    while game_status=="ON":
        clear_output()
        display()
        print("mr. {} man tell the place you wanna mark the {}  in(format:row column)".format(mark,mark))
        place_mark(mark)
        check(mark)
        if(check(mark)):
            game_status=="OFF"
            clear_output()
            display()
            print("PLAYER '{}' WINS!!".format(mark))
            break
        if mark==" X ":
            mark=" O "
        else:
            mark=" X "
        if len([x for x in lis if x.count("___")==0])==3:
            print("GAME TIED. NO ONE WINS")
            game_status="OFF"
        


# In[ ]:


print("WELCOME TO THE GAME OF TIC-TAC-TOE")
choice="Y"
lis=[[str("___") for y in range(0,3)] for x in range(0,3)]
count=3
while choice=="Y":
    print("DO YOU WANT TO PLAY THE GAME AGAIN?(Y:Yes/N:No)")
    choice=input().rstrip()
    if(choice =="Y"):
        gameplay()
    if(choice =="N"):
        print("COME BACK SOON!")


>>>>


# ## War Game!

# In[93]:


import random


# In[94]:


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[95]:


#CARD CLASS - Creating a single card
class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


# In[109]:


#DECK CLASS
class Deck:
    def __init__(self):
        self.all_cards=[]
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def draw_one(self):
        return self.all_cards.pop()
    
        
    


# >

# In[110]:


#PLAYER CLASS TO HOLD INSTANCES OF DECK CLASS I.E. THE CARDS
class Player:
    def __init__(self,name):
        self.name=name
        self.my_cards=[]
    
    def remove_one(self):
        return self.my_cards.pop(0)
    
    def add_cards(self,new_cards):
        if(type(new_cards)== type([])):
            self.my_cards.extend(new_cards)
        else:
            self.my_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.my_cards)} cards.'
        
    
        


# In[111]:


#WAR-GAME LOGIC and Game settings


# In[126]:


#SETTING UP THE GAME
new_deck=Deck()
new_deck.shuffle()


# In[127]:


print("enter name of player one")
player1= Player(input())
print("enter name of player two")
player2= Player(input())

print("Enter the number of cards to be bet for war!")
bet=int(input())


# In[128]:


#splitting the new deck:
for x in range(26):
    player1.my_cards.append(new_deck.draw_one())
    player2.my_cards.append(new_deck.draw_one())
    


# In[129]:


#Playing the Game


# In[130]:


import pdb


# In[131]:


status=True


# In[132]:


round_no=0
while status:
    round_no+=1
    print(f"Round {round_no}")
    
    if(len(player1.my_cards)==0):
        print(f"Player {player1.name} is out of cards! Player {player2.name} Wins!!")
        status=False
        break
    elif(len(player2.my_cards)==0):
        print(f"Player {player2.name} is out of cards! Player {player1.name} Wins!!")
        status=False
        break
    #else game goes on
    #starting individual rounds and resetting the cards on the table-
    player1_cards=[]
    player2_cards=[]
    player1_cards.append(player1.remove_one())
    player2_cards.append(player2.remove_one())


    #situation of war
    war=True
    while war:
    
        if(player1_cards[-1].value > player2_cards[-1].value):
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            war=False
    
        elif(player1_cards[-1].value < player2_cards[-1].value):
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            war=False
    
        else:
            print("At WAR!!")
    
        if(len(player1.my_cards) < bet):
            print(f"Player {player1.name} is unable to play war! Game over at War!")
            print(f"Player {player2.name} Wins! Player {player1.name} Loses!")
            status=False
            break
    
    
        elif(len(player2.my_cards) < bet):
            print(f"Player {player2.name} is unable to play war! Game over at War!")
            print(f"Player {player1.name} Wins! Player {player2.name} Loses!")
            status=False
            break
    
        else:
            for _ in range(bet):
                player1_cards.append(player1.remove_one())
                player2_cards.append(player2.remove_one())
    


        
    
    

        
        

        

        







