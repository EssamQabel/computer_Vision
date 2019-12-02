"""
THIS CODE IS AN UPDATED VERSION FROM DR.REDA M. HUSSIEN - FACULTY OF COMPUTERS AND INFORMATION, KAFRELSHEIKH UNIVERSITY -
FOR COMPUTER VISION COURSE.
"""

import math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


NUM_OF_PIXEL_VALUES = 256


def histogram(img):
    row, col = img.shape
    hist = np.zeros(NUM_OF_PIXEL_VALUES)
    for i in range(0, row):
        for j in range(0, col):
            try:
                hist[int(img[i, j])] += 1
            except:
                print(img[i, j])
    return hist


def linear_histogram_equalization(img, hmin, hmax):
    # values_dict = {}
    row, col = img.shape
    y = np.zeros((row, col))
    m = 255.0 / (hmax - hmin)
    for i in range(0, row):
        for j in range(0, col):
            if hmin <= img[i, j] <= hmax:
                y[i, j] = math.floor(m * (img[i, j] - hmin))
            elif img[i, j] > hmax:
                y[i, j] = NUM_OF_PIXEL_VALUES - 1
            else:
                y[i, j] = 0
    y = y.astype(int)
    # Nicely print the dictionary of values
    # for key, item in values_dict.items():
    #     print(str(key) + ' ' + str(int(item)))
    return y


def cumulative_histogram_equalization(img, hist=None):
    row, col = img.shape
    num_of_pixels = row * col
    if hist is None:
        hist = histogram(img)
    probability_of_pixels = [value / num_of_pixels for value in hist]
    cumulative_distribution = np.zeros(NUM_OF_PIXEL_VALUES)
    cumulative_distribution[0] = probability_of_pixels[0]
    for i in range(1, NUM_OF_PIXEL_VALUES):
        cumulative_distribution[i] = cumulative_distribution[i - 1] + probability_of_pixels[i]
    # Create new image
    new_image = np.zeros((row * col)).reshape((col, row))
    for i in range(0, row):
        for j in range(0, col):
            new_image[i, j] = math.floor((NUM_OF_PIXEL_VALUES - 1) * cumulative_distribution[img[i, j]])
    return new_image




