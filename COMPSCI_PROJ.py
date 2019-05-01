#############################################################################################################
## Group Name: Team Autoshade
## Members: I'munique Hill, Jeffery Shorter,and Lowell Wilson
## Date: 5/1/2019
## Description: This code allows for communication between the arduino and the Raspberry pi to create a manual mode of the blinds
#############################################################################################################
from Tkinter import *     #import tkinter for gui
import time                  # this is used for autoupdating gui which will be used for auto mode
import serial                # this is used to communicate with arduino via usb serial port

inputData = serial.Serial('/dev/ttyACM0', 9600) # any data sent or recieved is tied to this variable
class App():                                    # by using the serial port /dev/ttyACM0 at 9600 baud rate on raspberry pi
    def __init__(self, master):
        window.configure(background= 'black')   # sets background of whole window to black
        self.button1 = Button(master, text = "Increment", fg = "white", bg = "black", width = 65, command = self.say1)     # the increment buttom is placed on the bottom of the gui and it lowers the blinds
        self.button1.pack(side = BOTTOM)
        self.button2 = Button(master, text = "Decrement", fg = "white", bg = "black", width = 65, command = self.say2)   # the decrement button is placed on the bottom of the gui and it raises the blinds
        self.button2.pack(side = BOTTOM)
##        self.button3 = Button(master, text = "Display Outputs", fg = "white", bg = "black", width = 65, command = self.Say3)  #this portion is commented out due to it being buggy and crashe python this will be solved in
##        self.button3.pack(side = BOTTOM)
    def say1(self):             #function for data sending and button display
        inputData.write(b'0')    # converts string literal to byte of 0 for arduino to process
        label1 = Label(window, text = "Raising Blinds", fg = "white", bg = "black") # prints text 
        label1.pack(side = BOTTOM)  # prints it on the bottom
        window.destroy
    def say2(self):               #function for data sending and button display
        inputData.write(b'1')    # converts string literal to byte of 1 for ardiuno to process
        label2 = Label(window, text = "Lowering Blinds", fg = "white", bg = "black") # prints text
        label2.pack(side =BOTTOM) # prints it on the bottom
##    def Say3(self):
##        label3 = Label(window, text = inputData.readline(), fg = "white", bg = "black")     #this portion is commented out due to it being buggy and crashe python this will be solved in 
##        label3.pack(side = LEFT)                                                                               # a later version

##    def Add(event):                                                                                                      # this will be for future usage and we will modify this to work with auto mode
##       a = float(enter.get())
##        b = a + 1
##        labelresult = Label(window, text = inputData.readline()).grid(row = 4, column = 1)
##       return
window = Tk()
window.title("AutoShades Status")
app = App(window)
window.mainloop()
