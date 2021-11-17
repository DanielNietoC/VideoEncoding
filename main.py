from rgb_yuv import *
from run_length_encoding import *
from DCT import *

import matplotlib.pyplot as plt
import numpy as np
#import cv2
import subprocess
import pdb


if __name__ == '__main__':

    option = input("Choose exercise: ")
    if option == 1:
    #EXERCISE 1
        print("Exercise 1")
        r, g, b = input("Enter r, g, b values: ")

        print("Original rgb values: ", r, g, b)

        y, u, v = rgb_to_yuv(r, g, b)
        print("Converted yuv values: ", y, u, v)

        new_r, new_g, new_b = yuv_to_rgb(y, u, v)
        print("Reversed rgb values", new_r, new_g, new_b)


    if option == 2:
    #EXERCISE 2
        print("Exercise 2")
        #command written (on image location): ffmpeg -i mandril3.jpg -vf scale=320:240 mandril_320x240.jpg
        #new file created: mandril_320x240.jpg
        image_name = input("Write image's name and format in quotes "
                           "(Ex: 'mandril3.jpg'): ") # ask user for an image
        subprocess.call(["ffmpeg", "-i", str(image_name), "-vf",
                         "scale=320:240", "imageScaled.jpg"]) #call the terminal

    if option == 3:
    #EXERCISE 3 Consulted on https://stackoverflow.com/questions/10225403/how-can-i-extract-a-good-quality-jpeg-image-from-a-video-file-with-ffmpeg/10234065#10234065
        print("Exercise 3")
        #bw transform: ffmpeg -i mandril3.jpg -vf format=gray mandril3_bw.jpg
        #compression: ffmpeg -i mandril3_bw.jpg -qscale:v 31 mandril3_bw_comp.jpg
        image_name = input("Write image's name and format in quotes "
                           "(Ex: 'mandril3.jpg'): ")
        subprocess.call(["ffmpeg", "-i", str(image_name), "-vf",
                         "format=gray", "imageBW.jpg"]) #call the terminal

        subprocess.call(["ffmpeg", "-i", "imageBW.jpg", "-gscale:v", "31",
                         "imageComp.jpg"]) #call the terminal

    if option == 4:
    #EXERCISE 4
        print("Exercise 4")

        input_chain = input("Write in quotes the array to be encoded: ")
        print(runLengthEncoding(str(input_chain)))

    if option == 5:
    #EXERCISE 5
        print("Exercise 5")

        # For an array
        input_array = input("Write an array of floats (Ex: 4., 3., 5., 10.) : ")
        input_array = np.array(input_array)
        print("input array: ", input_array)

        input_dct = DCT(input_array)
        print("dct array: ", input_dct)

        decoded_dct = inverseDCT(input_dct)
        print("Decoded from dct: ", decoded_dct)


        # For a JPG image; In JPG the DCT has been already done

        # BGR_im = cv2.imread('mandril3.jpg')
        # im = cv2.cvtColor(BGR_im, cv2.COLOR_BGR2RGB) # From BGR to RGB
        # decoded_image = inverseDCT(im)
        #
        # plt.imshow(im)
        # plt.show()

                # The conversion from the JPG image is not correct.
                # It is not working on the correct channels,
                # but I still left the piece of code.

        # plt.imshow(decoded_image.astype('uint8'))
        # plt.show()

        # pdb.set_trace() # Debugging tool. Write q! to exit



