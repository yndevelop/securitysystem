#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 23:14:45 2021

@author: user
"""

known_users = ["Yahunathan","Aaron","Caleb", "Cody", "Megan", "Sarah" ]

while True:
    print("Hi! My name is Caleb")
    name = input("What is your name? ").strip().capitalize()
    
    if name in known_users:
        print("Hello {}!".format(name))
        remove =input("Would you like to be removed from the system (y/n)?:").lower()
        
    if remove == "y":
        known_users.remove(name)
    elif remove == "n":
        print("No problem, I am glad you stayed")
          
    else:
        print("Hmmm I don't think I have met you yet{}".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me == "y":
            known_users.append(name)  
        elif add_me == "n":
            print("No worries! I will see you around")
            
            
#D
    