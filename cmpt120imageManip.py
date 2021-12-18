# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author: Gursahib Singh Badwal
# Date: 05-12-2020
# Description: Here I have defined all the functions for doing manipulations to the provided image and these functions will be called in by the driver file named main.py
# Also this module will be imported in the main.py in order to call the functions from this module.
import cmpt120imageProj
import numpy


# Here I have defined the invert functions by reaching each pixel of the image and changing
#  it's RGB values by subtracting the RGB values of each pixel by 255 in order to get the 
# inverted RGB Values.
def invert(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel=img[x][y]
            pixel[0]=255-pixel[0]
            pixel[1]=255-pixel[1]
            pixel[2]=255-pixel[2]

# Here the flipHorizontal function has been defined which flips the image horizontally by firstly making 
# an copy of the left side of the image and then replacing the pixels as the left with the pixels on the 
# right with corresponding coordinates. Hnece, leading to the flipping of the image horizontally.
def flipHorizontal(img):
    for x in range((len(img))//2):
        for y in range(len(img[0])):
            left_half=img[x+1][y]
            img[x+1][y]=img[len(img)-x-1][y]
            img[len(img)-x-1][y]=left_half

# Similar procedure as that of the flipHorizontalfunction was used here 
# the only difference being that this time it was the upper half of the image which was saved
# and replaced by the pixels from the lower half and then the saved pixels from the top were pasted 
# to the lower half of the area.
def flipVertical(img):
    for x in range(len(img)):
        for y in range(len(img[0])//2):
            top_half=img[x][y+1]
            img[x][y+1]=img[x][len(img[0])-y-1]
            img[x][len(img[0])-y-1]=top_half

# this defined functions visits each pixel and replaces the R or red value of each pixel by 0 
# Therefore removing the red colour from the image
def remove_red(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel=img[x][y]
            pixel[0]=0   

# Similar to the remove red function but this time the G or green value was set 0.
def remove_green(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel=img[x][y]
            pixel[1]=0

# Blue or B value of each pixel was set to 0.
def remove_blue(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel=img[x][y]
            pixel[2]=0 

# Here the RGB values of each pixel is set to the average of R,G and B value of each pixel respectively.
# Resulting in a grayscale image like it was explained in the porject description.
def gray_scale(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel=img[x][y]
            pixel[0]=(pixel[0]+pixel[1]+pixel[2])/3
            pixel[1]=(pixel[0]+pixel[1]+pixel[2])/3
            pixel[2]=(pixel[0]+pixel[1]+pixel[2])/3
    return img

# The RGB Values of each pixel were modified as stated in the project description.
# Resulting in an image with a sepia filter apllied on it.
def sepia_filter(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel=img[x][y]
            SepiaRed=(pixel[0]*0.393)+(pixel[1]*0.769)+(pixel[2]*0.189)
            SepiaGreen=(pixel[0]*0.349)+(pixel[1]*0.686)+(pixel[2]*0.168)
            SepiaBlue=(pixel[0]*0.272)+(pixel[1]*0.534)+(pixel[2]*0.131)
            if SepiaRed>255:
                SepiaRed=255
            if SepiaGreen>255:
                SepiaGreen=255
            if SepiaBlue>255:
                SepiaBlue=255
            pixel[0]=SepiaRed
            pixel[1]=SepiaGreen
            pixel[2]=SepiaBlue

# In this fucntion if any of the R,G or B value was greater than or equal to 10
# then the value was decreased by 10 resulting in an overall decrease in the brightness of the image.
def decrease_brightness(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel=img[x][y]
            if pixel[0]>=10:
                pixel[0]-=10
            if pixel[1]>=10:
                pixel[1]-=10
            if pixel[2]>=10:
                pixel[2]-=10

# Here the RGB values were increased by 10 if they were less than or equal to 245.
def increase_brightness(img):
    for x in range(len(img)):
        for y in range(len(img[0])):
            pixel=img[x][y]
            if pixel[0]<=245:
                pixel[0]+=10
            if pixel[1]<=245:
                pixel[1]+=10
            if pixel[2]<=245:
                pixel[2]+=10

# Here first of all the createBlackImage function from a provided module was used in order to
# create a black image with dimensions being the opposite of the original image.(height being the width of the orignal image and width being the height of the orignal image)      
# Then the pixels from the orginal image were copied to this black image with a change in coordinates as per the project description.  
# As for rotating we were supposed to paste the pixels along the width of the new_img    
def rotate_left(img):
    width,height=len(img),len(img[0])
    new_img=cmpt120imageProj.createBlackImage(len(img[0]),len(img))
    for x in range(width):
        for y in range(height):
            pixel=img[x][y]
            new_img[y][width-x-1]=pixel
    img=new_img
    return img     

# Similar to the previous function with only difference being the pasting of pixels along height of the new_img instead
# of the width (like the rotate_left function)
def rotate_right(img):
    width,height=len(img),len(img[0])
    new_img=cmpt120imageProj.createBlackImage(len(img[0]),len(img))
    for x in range(width):
        for y in range(height):
            pixel=img[x][y]
            new_img[height-y-1][x]=pixel
    img=new_img
    return img   
    
# Multiple nested for lopps were used to access blocks of pixels(4x4) 
# and then taking the avearge of those group of pixels and then setting the RGB value of each 
# pixel as the avearge value obtained for that respective group.

def pixelate(img):
    red=0
    green=0
    blue=0
    for x in range(0,len(img)-len(img)%4,4):
        for y in range(0,len(img[0])-len(img[0])%4,4):
            for p in range(4):
                for q in range(4):
                    red+=img[x+p][y+q][0]
                    green+=img[x+p][y+q][1]
                    blue+=img[x+p][y+q][2]

            for p in range(4):
                for q in range(4):
                    img[x+p][y+q][0]=int(red)//16
                    img[x+p][y+q][1]=int(green)//16
                    img[x+p][y+q][2]=int(blue)//16
            red=0
            green=0
            blue=0


# This threshold_value has been defined in order to help the binarize function to work properly by receiving threshold value as a parameter.
# The threshold value has been obatianed by averaging and putting condiotnal at many points 
#Most important being the condtional used in the last to check if the difference between the 
# new_threshold value and the threshold is less than 10 or not and doing the required procedures 
# for both the Truth Values.           
def threshold_value(img):
    red_total=0
    img=gray_scale(img)

    for pixelRow in img:
        for pixel in pixelRow:
            red_total+=pixel[0]
    threshold_value=int(red_total/(len(img[0])*len(img)))
    background_threshold=0
    foreground_threshold=0
    background_count=0
    foreground_count=0
    new_threshold=0

    step=1

    while step==1:
        for pixelRow in img:
            for pixel in pixelRow:
                if pixel[0]>threshold_value:
                    background_threshold+=pixel[0]
                    background_count+=1
                else:
                    foreground_threshold+=pixel[0]
                    foreground_count+=1
        background_count=len(img)*len(img[0])
        foreground_count=len(img)*len(img[0])
        background_threshold_value=int(background_threshold/background_count)
        foreground_threshold_value=int(foreground_threshold/foreground_count)

        new_threshold=int((background_threshold_value+foreground_threshold_value)/2)
        if abs(new_threshold-threshold_value)<10:
            step=0
            
            
        background_threshold=0
        foreground_threshold=0
        background_count=0
        foreground_count=0
        return new_threshold       

# This function uses the result obtained from the previous function 
# if the red value(or any value bcoz all thress colours will have the same value due to the grayscale applied)
# is greater than the threshold value then the RGB values are set to 255 resulting in a white pixel
# and the RGB values are turned to 0 for the contrary case and the pixel becomes black
def binarize(img,threshold):
    gray_scale(img)
    for pixelRow in img:
        for pixel in pixelRow:
            if pixel[0]>threshold:
                for i in range(3):
                    pixel[i]=255
            else:
                for i in range(3):
                    pixel[i]=0
    return img
            


    
    





            




            