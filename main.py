# CMPT 120 Yet Another Image Processer
# Starter code for main.py
# Author(s):
# Date:
# Description:

import cmpt120imageProj
import cmpt120imageManip
import tkinter.filedialog
import pygame
pygame.font.init()

# list of system options
system = [
            "Q: Quit",
            "O: Open Image",
            "S: Save Current Image",
            "R: Reload Original Image"
         ]

# list of basic operation options
basic = [
          "1: Invert",
          "2: Flip Horizontal",
          "3: Flip Vertical",
          "4: Switch to Intermeidate Functions",
          "5: Switch to Advanced Functions"
         ]

# list of intermediate operation options
intermediate = [
                  "1: Remove Red Channel",
                  "2: Remove Green Channel",
                  "3: Remove Blue Channel",
                  "4: Convert to Grayscale ",
                  "5: Apply Sepia Filter",
                  "6: Decrease Brightness",
                  "7: Increase Brightness",
                  "8: Switch to Basic Functions",
                  "9: Switch to Advanced Functions"
                 ]

# list of advanced operation options
advanced = [
                "1: Rotate Left",
                "2: Rotate Right",
                "3: Pixelate",
                "4: Binarize",
                "5: Switch to Basic Functions",
                "6: Switch to Intermediate Functions"
             ]

# a helper function that generates a list of strings to be displayed in the interface
def generateMenu(state):
    """
    Input:  state - a dictionary containing the state values of the application
    Returns: a list of strings, each element represets a line in the interface
    """
    menuString = ["Welcome to CMPT 120 Image Processer!"]
    menuString.append("") # an empty line
    menuString.append("Choose the following options:")
    menuString.append("") # an empty line
    menuString += system
    menuString.append("") # an empty line

    # build the list differently depending on the mode attribute
    if state["mode"] == "basic":
        menuString.append("--Basic Mode--")
        menuString += basic
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-5)..")
    elif state["mode"] == "intermediate":
        menuString.append("--Intermediate Mode--")
        menuString += intermediate
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-9)..")
    elif state["mode"] == "advanced":
        menuString.append("--Advanced Mode--")
        menuString += advanced
        menuString.append("")
        menuString.append("Enter your choice (Q/O/S/R or 1-6)..")
    else:
        menuString.append("Error: Unknown mode!")

    return menuString

# a helper function that returns the result image as a result of the operation chosen by the user
# it also updates the state values when necessary (e.g, the mode attribute if the user switches mode)
def handleUserInput(state, img):
    """
        Input:  state - a dictionary containing the state values of the application
                img - the 2d array of RGB values to be operated on
        Returns: the 2d array of RGB vales of the result image of an operation chosen by the user
    """
    userInput = state["lastUserInput"].upper()
    # handle the system functionalities
    if userInput.isalpha(): # check if the input is an alphabet
        print("Log: Doing system functionalities " + userInput)
        if userInput == "Q": # this case actually won't happen, it's here as an example
            print("Log: Quitting...")
        # Here some condtions have been stated to make the program work according to the input if the user 
        # Like O,S and R
        elif userInput=="O":
            tkinter.Tk().withdraw()
            openFilename=tkinter.filedialog.askopenfilename()
            img=cmpt120imageProj.getImage(openFilename)
            appStateValues["lastOpenFilename"]=openFilename
            cmpt120imageProj.showInterface(img,"Original Image",generateMenu(appStateValues))
            # This is to open an image from the user files

        elif userInput=="S":
            tkinter.Tk().withdraw()
            saveFilename= tkinter.filedialog.asksaveasfilename()
            cmpt120imageProj.saveImage(img,saveFilename)
            cmpt120imageProj.showInterface(img,"Final Image", generateMenu(appStateValues))
            # This is to save the image to the user memory area.

        elif userInput=="R":
            tkinter.Tk().withdraw()
            openFilename=appStateValues["lastOpenFilename"]
            img=cmpt120imageProj.getImage(openFilename)
            cmpt120imageProj.showInterface(img,"Original Image",generateMenu(appStateValues))
            # This is to get back to the orginal image.
                    # ***add the rest to handle other system functionalities***

    # or handle the manipulation functionalities based on which mode the application is in
    elif userInput.isdigit(): # has to be a digit for manipulation options
        print("Log: Doing manipulation functionalities " + userInput)
        # ***add the rest to handle other manipulation functionalities***
        if appStateValues["mode"]=="basic":
            if userInput=="1":
                tkinter.Tk().withdraw()
                cmpt120imageManip.invert(img)
                cmpt120imageProj.showInterface(img,"Inverted Image",generateMenu(appStateValues))

            elif userInput=="2":
                tkinter.Tk().withdraw()
                cmpt120imageManip.flipHorizontal(img)
                cmpt120imageProj.showInterface(img,"Flip Horizontal Image",generateMenu(appStateValues))

            elif userInput=="3":
                tkinter.Tk().withdraw()
                cmpt120imageManip.flipVertical(img)
                cmpt120imageProj.showInterface(img,"Flip Vertical Image",generateMenu(appStateValues))
            
            elif userInput=="4":
                tkinter.Tk().withdraw()
                appStateValues["mode"]="intermediate"
                cmpt120imageProj.showInterface(img,"Intermediate Menu",generateMenu(appStateValues))
                # This is coded to allow the user to enter the Intermediate menu.

            elif userInput=="5":
                tkinter.Tk().withdraw()
                appStateValues["mode"]="advanced"
                cmpt120imageProj.showInterface(img,"Advanced Menu",generateMenu(appStateValues))
                # This is coded to allow the user to enter the Advanced menu.

        # So here the functions defined in the Manip module are called and are used to manipulate the image 
        # accroding to the user Input while the user selecting Basic Functions

        elif appStateValues["mode"]=="intermediate":
            if userInput=="1":
                tkinter.Tk().withdraw()
                cmpt120imageManip.remove_red(img)
                cmpt120imageProj.showInterface(img,"Red Channel Removed",generateMenu(appStateValues))

            elif userInput=="2":
                tkinter.Tk().withdraw()
                cmpt120imageManip.remove_green(img)
                cmpt120imageProj.showInterface(img,"Green Channel Removed",generateMenu(appStateValues))

            elif userInput=="3":
                tkinter.Tk().withdraw()
                cmpt120imageManip.remove_blue(img)
                cmpt120imageProj.showInterface(img,"Blue Channel Removed",generateMenu(appStateValues))

            elif userInput=="4":
                tkinter.Tk().withdraw()
                cmpt120imageManip.gray_scale(img)
                cmpt120imageProj.showInterface(img,"Grayscale Image",generateMenu(appStateValues))

            elif userInput=="5":
                tkinter.Tk().withdraw()
                cmpt120imageManip.sepia_filter(img)
                cmpt120imageProj.showInterface(img,"Sepia Filter Applied Image",generateMenu(appStateValues))

            elif userInput=="6":
                tkinter.Tk().withdraw()
                cmpt120imageManip.decrease_brightness(img)
                cmpt120imageProj.showInterface(img,"Brightness Decreased",generateMenu(appStateValues))
            
            elif userInput=="7":
                tkinter.Tk().withdraw()
                cmpt120imageManip.increase_brightness(img)
                cmpt120imageProj.showInterface(img,"Brightness Decreased",generateMenu(appStateValues))

            elif userInput=="8":
                tkinter.Tk().withdraw()
                appStateValues["mode"]="basic"
                cmpt120imageProj.showInterface(img,"Basic Menu",generateMenu(appStateValues))
                # This is coded to allow the user to enter the Basic Menu

            elif userInput=="9":
                tkinter.Tk().withdraw()
                appStateValues["mode"]="advanced"
                cmpt120imageProj.showInterface(img,"Advanced Menu",generateMenu(appStateValues))
                # This is coded to allow the user to enter the Advanced menu.
        # Here the functions under the intermediate category have been called to manipulate the image accordingly.

        elif appStateValues["mode"]=="advanced":
            if userInput=="1":
                tkinter.Tk().withdraw()
                new_img=cmpt120imageManip.rotate_left(img)
                cmpt120imageProj.showInterface(new_img,"Left Rotated Image",generateMenu(appStateValues))

            elif userInput=="2":
                tkinter.Tk().withdraw()
                new_img=cmpt120imageManip.rotate_right(img)
                cmpt120imageProj.showInterface(new_img,"Right Rotated Image",generateMenu(appStateValues))

            elif userInput=="3":
                tkinter.Tk().withdraw()
                cmpt120imageManip.pixelate(img)
                cmpt120imageProj.showInterface(img,"Pixelated Image",generateMenu(appStateValues))

            elif userInput=="4":
                tkinter.Tk().withdraw()
                thresh_value=cmpt120imageManip.threshold_value(img)
                new_img=cmpt120imageManip.binarize(img,thresh_value)
                cmpt120imageProj.showInterface(new_img,"Binarize Image",generateMenu(appStateValues))

            elif userInput=="5":
                tkinter.Tk().withdraw()
                appStateValues["mode"]="basic"
                cmpt120imageProj.showInterface(img,"Basic Menu",generateMenu(appStateValues))
                # This is coded to allow the user to enter the Basic Menu.

            elif userInput=="6":
                tkinter.Tk().withdraw()
                appStateValues["mode"]="intermediate"
                cmpt120imageProj.showInterface(img,"Intermediate Menu",generateMenu(appStateValues))
                # This is coded to allow the user to enter the Intermediate menu.
        # Here the functions under the advanced category have been called to do the necessary work which the user wants.    
            





    else: # unrecognized user input
            print("Log: Unrecognized user input: " + userInput)

    return img

# use a dictionary to remember several state values of the application
appStateValues = {
                    "mode": "basic",
                    "lastOpenFilename": "",
                    "lastSaveFilename": "",
                    "lastUserInput": ""
                 }

currentImg = cmpt120imageProj.createBlackImage(600, 400) # create a default 600 x 400 black image
cmpt120imageProj.showInterface(currentImg, "No Image", generateMenu(appStateValues)) # note how it is used

# ***this is the event-loop of the application. Keep the remainder of the code unmodified***
keepRunning = True
# a while-loop getting events from pygame
while keepRunning:
    ### use the pygame event handling system ###
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            appStateValues["lastUserInput"] = pygame.key.name(event.key)
            # prepare to quit the loop if user inputs "q" or "Q"
            if appStateValues["lastUserInput"].upper() == "Q":
                keepRunning = False
            # otherwise let the helper function handle the input
            else:
                currentImg = handleUserInput(appStateValues, currentImg)
        elif event.type == pygame.quit: #another way to quit the program is to click the close botton
            keepRunning = False

# shutdown everything from the pygame package
pygame.quit()

print("Log: Program Quit")