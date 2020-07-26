# Course:           CS4242
# Student name:     Timmy Duong
# Student ID:       000678536
# Assignment #:     3
# Due Date:         July 1
# Signature:        
# Score:            

import tkinter as tk
from random import *
import numpy as np


class Perceptron:
    def IsBright():
        image = np.random.choice([-1, 1], size = gridSize) # random numbers of -1 or 1
        Perceptron.CanvasBuilder(image) # make the checkerboard-like tiles
        # +1 for bright, -1 for dark

        #print(image)
        """
        random_weight = np.random.uniform(-1, 1, size=4) # random weight of -1 to 1. 1x4 array
        for i in random_weight:
            rounded_weight = np.around(random_weight, 2)
        """
        output_value = 0
        weight = 0.25

        for num in image.flatten(): # flatten 2D into 1D array
            output_value += (weight * num)
        Perceptron.PrintSol(output_value)

    def PrintSol(output_value):
        if (output_value > -0.1):
            #msg = tk.Label(root, text = "[Output] Image is bright with value " + str(output_value))
            #msg.pack(side = "bottom")
            print("Image is bright with value {}." .format(output_value))
        else:
            #msg = tk.Label(root, text = "[Output] Image is dark with value " + str(output_value))
            #msg.pack(side = "bottom")
            print("Image is dark with value {}." .format(output_value))


    def CanvasBuilder(image):
        for i in range(row):
            for j in range(col):
                if (image[j][i] == -1): # switch i and j so that it would match actual print statement of image
                    canvas.create_rectangle(i * 100, j * 100, (i * 100) + 100, (j * 100) + 100, fill = 'black', outline = 'gray', width = 2)
                elif (image[j][i] == 1):
                    canvas.create_rectangle(i * 100, j * 100, (i * 100) + 100, (j * 100) + 100, fill = 'white', outline = 'gray', width = 2)

root = tk.Tk()
root.title("Perceptron")
row, col = 2, 2
gridSize = (2, 2)
canvas = tk.Canvas(root, width = 350, height = 350, borderwidth = 1, relief = 'raised')
canvas.pack(side = "left")

key = tk.Label(root, text = "Key: \nBlack = -1.\n White = +1.")
key.pack(side = "top")
button1 = tk.Button(root, text = "Next Input.", fg = 'red', command = Perceptron.IsBright)
button1.pack(side = "bottom")
clear = tk.Button(root, text = 'Clear', command = lambda: (canvas.delete("all")))
clear.pack(side = "bottom")

Perceptron.IsBright()

root.mainloop()