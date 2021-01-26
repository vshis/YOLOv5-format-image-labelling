import numpy as np
import cv2
import os

imageSize = [512, 512]  #Size of the image in Pixels [x,y]
massiv = []

class Cone:
    def __init__(self, color, x_centre, y_centre, x_width, y_height, imgIndex):
        self.color = color 
        self.x_centre = x_centre
        self.y_centre = y_centre
        self.x_width = x_width
        self.y_height = y_height    
        self.imgIndex = imgIndex

        
class Color: 
    BLUE = 0
    ORANGE = 1
    YELLOW = 2


def construct_txt(path):
    images = {}
    for cone in massiv:
        if not images.get(cone.imgIndex):
            images[cone.imgIndex] = []
        images[cone.imgIndex].append(cone)
        
    for imgIndex in images:
        text = ''
        for cone in images[imgIndex]:
            text += f'{cone.color} {cone.x_centre} {cone.y_centre} {cone.x_width} {cone.y_height}\n'
            
        with open(f'{path}/{imgIndex}.txt', 'w') as txt_file:
            txt_file.write(text)
    
def operateImage(path):
    print(path)
    image = cv2.imread(path)
    pixels = np.argwhere(image == 255)  #Record the positions of all the white pixels
    minY = min(pixels[:,0]) #MINIMUM Y COORDINATE 
    maxY = max(pixels[:,0]) #MAX Y COORDINATE 
    minX = min(pixels[:,1]) #MINIMUM X cord
    maxX = max(pixels[:,1]) #MAX X cord
    
    centreY = (minY+maxY)/2
    centreX = (minX+maxX)/2
    height = maxY - minY
    width = maxX - minX
    
    #YOLO FORMATTING
    centreYoloY = centreY/imageSize[1]
    centreYoloX = centreX/imageSize[0]
    heightYolo = height/imageSize[1]
    widthYolo = width/imageSize[0]
    
    if path.count('blue'):
        color = Color.BLUE
    elif path.count('orange'):
        color = Color.ORANGE
    else:
        color = Color.YELLOW
    
    imgIndex = path.split('/')[-1].split('_')[0]
    massiv.append(Cone(color, centreYoloX, centreYoloY, widthYolo, heightYolo, imgIndex))
    
    
    #To show the modified image

def recursiveFind(path):
    for file in os.listdir(path):
        if file.endswith('.png') and file.count('_')>=1:            
            operateImage(f'{path}/{file}')
            os.remove(f'{path}/{file}')
        elif not file.count('.'):
            recursiveFind(f'{path}/{file}')

if __name__ == '__main__':
    mainPath = 'C:/apps/synthConesTest/captures'
    recursiveFind(mainPath)
    construct_txt(mainPath)






