# Course:           CS4242
# Student name:     Timmy Duong
# Student ID:       000678536
# Assignment #:     2
# Due Date:         June 27
# Signature:           
# Score:            

from tkinter import *

root = Tk()
val1 = IntVar()

class NQueens:

    def checking(row, column):
        # checking for the rows and columns across and down using j iterator
        for j in range(0, size):
            if board[row][j] == 1 or board[j][column] == 1:
                return True
        # checking for the rows and columns diagonally using k and l iterators
        for k in range(0, size):
            for l in range(0, size):
                while row > 0 and column > 0:
                    row -= 1
                    column -= 1
                    k = row
                    l = column
                    if board[k][l] == 1:
                        return True
        return False
    def solve(n):
        goal = 0
        # if n is 0, problem cannot be solved, goal failed
        if n == 0:
            return True
        # else, problem can be solved, goal can be reached
        for row in range(0, size):
            for column in range(0, size):
                if (not(NQueens.checking(row, column))) and (board[row][column] != 1):
                    board[row][column] = 1
                    # recursion
                    if (NQueens.solve(n-1) == True):
                        return True
                    board[row][column] = 0
        return False

    def printBoard(board):
        for i in board:
            print(i)

    def getBoard():
        printB = NQueens.printBoard(board)


root.geometry("400x150")
label1 = Label(root, text = "Solve N-Queen")
label1.pack(side = "top")
b1 = Radiobutton(root, variable = val1, value = 1, text = "8 x 8", pady = 20)
b1.pack(side = "top")
button1 = Button(root, text = "Solve", width = 10, command = NQueens.getBoard)
button1.pack(side = "top")

size = 8
board = [[0] * size for x in range(size)]
NQueens.solve(size)

root.mainloop()


