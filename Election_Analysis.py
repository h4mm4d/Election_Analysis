# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:13:53 2021

@author: Hammad Rahman

"""
choice = input ("(r)rock (p)paper or (s)cissors?")
import random
Comp_choice == random.choice(["r","p","s"])
print (Comp_choice)
    if choice == Comp_choice:
           print ("its a draw")
    elif choice == "r" and Comp_choice == "s"
           print ("You won!")
    elif choice == "p" and Comp_choice == "r"
           print ("You won!")
    elif choice == "s" and Comp_choice == "p"
       print ("You won!")
    else:
       print ("sorry, you lose")
