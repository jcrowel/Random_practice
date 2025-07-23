#!/usr/bin/env python
# coding: utf-8

# In[1]:


def coffee_machine(order):
    global water
    global coffee
    global milk
    global keepgoing
    
    global quarters
    global dimes
    global nickels 
    global pennies
    
    if order == "latte":
        p_quarters = float(input("how many quarters are you paying with? "))
        p_dimes= float(input(" how many dimes are you paying with? "))
        p_nickels = float(input("how many nickels are you paying with? "))
        p_pennies = float(input("how many pennies are you paying with? "))

        q= quarters * p_quarters
        d= dimes * p_dimes
        n= nickels * p_nickels
        p = pennies * p_pennies
        total = 2.5
        p_total= q + d + n + p
    
        
        if water< 200:
            print(f"not enough water. please replace water and come back. Here is your ${p_total} back.")
            keepgoing= False

        elif milk< 150:
            print(f"not enough milk. please replace milk and come back. Here is your ${p_total} back.")
            keepgoing = False

        elif coffee < 24:
            print(f"not enough coffee. please replace and come back. Here is your ${p_total} back.")
            keepgoing= False
            
        elif p_total< total:
            refund= round(total- p_total,2)
            print(f"you still need ${refund} amount. here's your ${p_total} back.come back when you have more money ")

        elif p_total > total:
            amount_back= round(p_total - total,2)
            print(f"You overpaid. you get ${amount_back} back. enjoy your drink")
            water = water -200
            milk = milk - 150
            coffee = coffee - 24 
            
        else: 
            print("enjoy your drink")
            water = water -200
            milk = milk - 150
            coffee = coffee - 24 


    if order == "espresso":
        p_quarters = float(input("how many quarters are you paying with? "))
        p_dimes= float(input(" how many dimes are you paying with? "))
        p_nickels = float(input("how many nickels are you paying with? "))
        p_pennies = float(input("how many pennies are you paying with? "))

        q= quarters * p_quarters
        d= dimes * p_dimes
        n= nickels * p_nickels
        p = pennies * p_pennies
        total = 1.5
        p_total= q + d + n + p


        if coffee < 12:
            print(f"not enough coffee. please replace and come back. Here is your ${p_total} back.")
            keepgoing= False

        elif water < 50:
            print(f"not enough water. please replace water and come back. here is your {p_total} back.")
            keepgoing= False        

        elif p_total< total:
            refund= round(total- p_total,2)
            print(f"you still need ${refund} amount. here's your ${p_total} back. come back when you have more money ")
        elif p_total > total:
            amount_back= round(p_total - total,2)
            print(f"You overpaid. you get ${amount_back} back. enjoy your drink")
            water = water - 50
            coffee = coffee - 12
        else: 
            print("enjoy your drink")
            water = water - 50
            coffee = coffee - 12

    if order == "cappuccino":
        p_quarters = float(input("how many quarters are you paying with? "))
        p_dimes= float(input(" how many dimes are you paying with? "))
        p_nickels = float(input("how many nickels are you paying with? "))
        p_pennies = float(input("how many pennies are you paying with? "))

        q= quarters * p_quarters
        d= dimes * p_dimes
        n= nickels * p_nickels
        p = pennies * p_pennies
        total = 3.0
        p_total= q + d + n + p

        if water< 250:
            keepgoing= False
            print(f"not enough water. please replace water and come back. Here is your ${p_total} back.")
            
        elif milk< 100:
            keepgoing = False
            print(f"not enough milk. please replace milk and come back. Here is your ${p_total} back.")
            
        
        elif coffee < 24:
            keepgoing= False
            print(f"not enough coffee. please replace and come back. Here is your ${p_total} back.")
            

        elif p_total< total:
            refund= round(total- p_total,2)
            print(f"you still need ${refund} amount. here's your ${p_total} back.come back when you have more money ")
        
        elif p_total > total:
            amount_back= round(p_total - total,2)
            print(f"You overpaid. you get ${amount_back} back. enjoy your drink")
            water = water - 250
            milk = milk - 100
            coffee = coffee - 24 

        else: 
            print("enjoy your drink")
            water = water -250
            milk = milk - 100
            coffee = coffee - 24 


    if order== 'report':
        print(water)
        print(milk)
        print(coffee)


# In[ ]:


print("welcome to the coffee machine")
print("We offer 'espresso', 'latte', and 'cappuccino'")
#print(Menu)
water= 500
milk= 600
coffee= 144

quarters = 0.25
dimes= 0.10
nickels = 0.05
pennies= 0.01


keepgoing = True
while keepgoing== True:
    order= input("what would you like to drink? ")
    coffee_machine(order)


# In[ ]:




