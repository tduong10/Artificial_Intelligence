# Course:           CS4242
# Student name:     Timmy Duong
# Student ID:       000678536
# Assignment #:     1
# Due Date:         June 10
# Signature:        
# Score:            

# Implement a performance-measuring environment simulator for the vacuum-cleaner world depicted in Figure 2.2 and specified on page 38. 
# Your implementation should be modular so that the sensors, actuators, and environment characteristics (size, shape, dirt placement, etc.) can be changed easily. 
# (Note: for some choices of programming language and operating system there are already implementations in the online code repository.)

import tkinter as tk
from tkinter import *
import random

root = Tk()
root.title("Simple Reflex Agent")
root.geometry("500x500")

class Vacuum():
    def __init__(self):     
        self.statusA = 0
        self.statusB = 0
        # randomize dirt status. 1 being dirty and 0 being clean
        self.statusA = random.randint(0, 1)
        self.statusB = random.randint(0, 1)
        total_steps = 2 # default of 2
        reward = 0
        # randomize location of vacuum
        vacuum_loc = random.randint(0, 1)
        canvas = Canvas(root, width = 250, height = 200, bg = "aliceblue")
    
        if (vacuum_loc == 0):
            label1 = Label(root, text = "The vacuum randomly placed at A.")
            label1.pack(side = "top")
            l = Label(root, text = "Location A")
            l.pack(side = "bottom")
            # black rectangle is the vacuum
            vacuum = canvas.create_rectangle(70, 70, 40, 40, fill = "black")
            canvas.pack(side = "bottom") 
            # A location
            if(self.statusA) == 1:
                label2 = Label(root, text = "Spot A is dirty.")
                label2.pack(side = "top")
                dirt = canvas.create_oval(20, 20, 10, 10, fill = "green")
                canvas.pack(side = "bottom")
                self.statusA == 0
                reward += 1
                label3 = Label(root, text = "Spot A is cleaned.")
                label3.pack(side = "top")
                label4 = Label(root, text = "Moving to next location.")
                label4.pack(side = "top")
            # B location
            if(self.statusB == 1):
                label5 = Label(root, text = "Spot B is dirty.")
                label5.pack(side = "top")
                dirt = canvas.create_oval(20, 20, 10, 10, fill = "green")
                self.statusB = 0
                reward += 1
                label6 = Label(root, text = "Spot B is cleaned.")
                label6.pack(side = "top")
            
    
        elif (vacuum_loc == 1):
            label7 = Label(root, text = "The vacuum randomly placed at B.")
            label7.pack(side = "top")
            l = Label(root, text = "Location B")
            l.pack(side = "bottom")
            vacuum = canvas.create_rectangle(70, 70, 40, 40, fill = "black")
            canvas.pack(side = "bottom") 
            # B location
            if (self.statusB == 1):
                label8 = Label(root, text = "Spot B is dirty")
                label8.pack(side = "top")
                dirt = canvas.create_oval(20, 20, 10, 10, fill = "green")
                canvas.pack(side = "bottom")
                self.statusB == 0
                reward += 1
                label9 = Label(root, text = "Spot B is cleaned.")
                label9.pack(side = "top")
                label10 = Label(root, text = "Moving to next location.")
                label10.pack(side = "top")
            # A location
            if (self.statusA == 1):
                label11 = Label(root, text = "Spot A is dirty.")
                dirt = canvas.create_oval(20, 20, 10, 10, fill = "green")
                label11.pack(side = "top")
                self.statusA = 0
                label12 = Label(root, text = "Spot A is cleaned.")
                label12.pack(side = "top")
                reward += 1
            
        total = reward     
        label13 = Label(root, text = "Reward: " + str(total))
        label13.pack(side = "top")    
        performance = (reward / total_steps) * 100
        label14 = Label(root, text = "Performance Score: " + str(performance))
        label14.pack(side = "top")

# call to run 
Vacuum()
# mainloop() is a method on the main window which we execute when we want to run our application
root.mainloop()