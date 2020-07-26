# Course:           CS4242
# Student name:     Timmy Duong
# Student ID:       000678536
# Assignment #:     3
# Due Date:         July 1
# Signature:        
# Score:            

import tkinter as tk
import numpy as np
import math
from random import *

# reminder python class's functions need 'self'
class ANN:

    def InputLayer():
        # input image
        image = np.random.choice([-1, 1], size = (2, 2)) # random numbers of -1 or 1
        # +1 for bright, -1 for dark

        l_rate = 0.1

        # hidden layer
        first_hidden = 0
        second_hidden = 0
        third_hidden = 0
        fourth_hidden = 0

        img_size = 4
        for num1 in image.flatten(): # flatten 2D into 1D array
            first_hidden += (ANN.Rand_Weights(img_size) * num1) * l_rate
        
        for num2 in image.flatten(): # flatten 2D into 1D array
            second_hidden += (ANN.Rand_Weights(img_size) * num2) * l_rate

        for num3 in image.flatten(): # flatten 2D into 1D array
            third_hidden += (ANN.Rand_Weights(img_size) * num3) * l_rate

        for num4 in image.flatten(): # flatten 2D into 1D array
            fourth_hidden += (ANN.Rand_Weights(img_size) * num4) * l_rate

        total1 = (first_hidden + second_hidden)
        total2 = (third_hidden + fourth_hidden)
        ANN.HiddenLayer(total1, total2)

    def Rand_Weights(arraySize):
        random_weight = np.random.uniform(-0.5, 0.5, size=arraySize) # random weight of -0.5 to 0.5
        for i in random_weight:
            rounded_weight = np.around(random_weight, 2) # hundredths place
        return rounded_weight

    def Sigmoid_Func(x):
        sigmoid = 1 / (1 + np.exp(-x))
        return sigmoid

    def HiddenLayer(one, two):

        first_out = ANN.Sigmoid_Func(one)
        second_out = ANN.Sigmoid_Func(two)

        size = 1
        first_out *= ANN.Rand_Weights(size) 
        second_out *= ANN.Rand_Weights(size) 

        ANN.OutputLayer(first_out, second_out)

    def OutputLayer(one, two):
        first_out = ANN.Sigmoid_Func(one)
        second_out = ANN.Sigmoid_Func(two)

        ANN.Sigmoid_Deriv(first_out, second_out)    

    def Sigmoid_Deriv(x, y):
        first_err = x * (1 - x)
        second_err = y * (1 - y)
        
        ANN.Epochs(first_err, second_err)

    def Epochs(one, two):
        error = one + two
        print(error)



root = tk.Tk()
root.title("Neural Network")
canvas = tk.Canvas(root, width = 300, height = 300, borderwidth = 1)
canvas.pack(side = "top")
button1 = tk.Button(root, text = "Start", fg = 'red', command = ANN.InputLayer)
button1.pack(side = "bottom")

root.mainloop()