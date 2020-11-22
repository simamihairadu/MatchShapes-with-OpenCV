import cv2
import numpy as np

class Shape():
    name = 0;
    filePath = 0;
    value = 0;

    def __init__(self,name,filePath):
        self.name = name
        self.filePath = filePath;


def SetUp():
    shapeArray = []
    shapeArray.append(Shape('rectangle', 'E:/info/Procesarea Imaginilor/Shapes/rectangle.png'))
    shapeArray.append(Shape('star', 'E:/info/Procesarea Imaginilor/Shapes/star.png'))
    shapeArray.append(Shape('circle', 'E:/info/Procesarea Imaginilor/Shapes/circle.png'))
    shapeArray.append(Shape('bottle','E:/info/Procesarea Imaginilor/Shapes/bottle.png'))
    shapeArray.append(Shape('hand','E:/info/Procesarea Imaginilor/Shapes/hand.jpg'))
    return shapeArray


