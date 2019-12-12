# import the necessary packages
import cv2
from color_coordinate_detector.DetectColor import master_runner


class RectangleDetector:
    def __init__(self):
        pass

    def detect(self, c):
        print("second class called")

        # initialize the shape name and approximate the contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        # at .04
        approx = cv2.approxPolyDP(c, 0.01 * peri, True)

        # if the shape is a triangle, it will have 3 vertices
        if len(approx) == 3:
            shape = "triangle"

        # if the shape has 4 vertices, it is either a square or
        # a rectangle
        elif len(approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)
            print("bounds found")
            topLeft = [y + h, x]
            topRight = [y, x]
            botRight = [y, x + w]
            botLeft = [y + h, x + w]

            array = [topLeft, topRight, botRight, botLeft]
            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle

            if ar >= 0.85 and ar <= 1.15:
                shape = "square"
            elif ((x != 0) and (y != 0)):
                # this one is the possible bounding rectangle, back in detect_shapes, it will find the largest of many and determine
                # the actual bounds for the pattern
                shape = "rectangle"

            else:
                shape = "original rectangle but we dont care about this one"

        # if the shape is a pentagon, it will have 5 vertices
        elif len(approx) == 5:
            shape = "pentagon"

        # otherwise, we assume the shape is a circle
        else:
            shape = "circle"

        # return the name of the shape
        # return shape

        # returns array of coordinates
        return array
