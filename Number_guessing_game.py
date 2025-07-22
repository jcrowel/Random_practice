#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[ ]:


#Number guessing game

print (" Welcome to the number guessing game")

number = random.randint(1,100)
print(number)

difficulty = input(" Would you like to play on 'easy' or 'hard' mode?  ")
print(difficulty)
turns =0 
keepgoing = True

if difficulty == 'hard':
    print(" you have 5 guesses")
    #number_of_guesses= 5
    guess= int(input("guess a number between 1-100: "))
    turns= 5

    while keepgoing== True:
        for turn in range(turns):
            if guess > number:
                turns= turns-1
                print(f"Too high. you have {turns} guesses left")
                guess= int(input(" guess again: "))
            
            elif guess < number:
                turns= turns -1
                print(f" Too Low. you have {turns} guesses left")
                guess = int(input("guess again: "))
            else:
                turns= 0
                keepgoing = False
    print("you got it")
            

if difficulty == 'easy':
    print(" you have 10 guesses")
    #number_of_guesses= 5
    guess= int(input("guess a number between 1-100"))
    turns = 10

    while keepgoing== True:
        for i in range(turns):
            if guess > number:
                turns = turns-1
                print(f"Too high. you have {turns} guesses left")
                guess= int(input(" guess again: "))
            
            elif guess < number:
                turns = turns -1
                print(f" Too Low. you have {turns} guesses left")
                guess = int(input("guess again: "))
            else: 
                turns =0 
                keepgoing = False
    print("you got it")
            

