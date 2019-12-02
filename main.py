import computer_vision as cv
import math
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


def using_linear_histogram_equalization():
    image = Image.open('historignal.jpg').convert("L")
    img = np.asarray(image)

    # Get and display the image.
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')

    # Create the histogram for the first image.
    hist = cv.histogram(img)
    x = np.arange(0, 256)

    plt.subplot(2, 2, 2)
    plt.bar(x, hist, color='b', width=5, align='center')

    # Create and display the new created image.
    new_image = cv.linear_histogram_equalization(img, 102, 148)
    img = np.asarray(new_image)

    plt.subplot(2, 2, 3)
    plt.imshow(new_image, cmap='gray')

    # Create the histogram for the newly created image.
    new_hist = cv.histogram(img)

    plt.subplot(2, 2, 4)
    plt.bar(x, new_hist, color='b', width=5, align='center')

    plt.show()


def using_cumulative_histogram_equalization():
    image = Image.open('historignal.jpg').convert("L")
    img = np.asarray(image)

    # Get and display the image.
    plt.subplot(2, 2, 1)
    plt.imshow(image, cmap='gray')

    # Create the histogram for the first image.
    hist = cv.histogram(img)
    x = np.arange(0, 256)

    plt.subplot(2, 2, 2)
    plt.bar(x, hist, color='b', width=5, align='center')

    # Create and display the new created image.
    new_image = cv.cumulative_histogram_equalization(img)

    plt.subplot(2, 2, 3)
    plt.imshow(new_image, cmap='gray')

    # Create the histogram for the newly created image.
    new_hist = cv.histogram(new_image)

    plt.subplot(2, 2, 4)
    plt.bar(x, new_hist, color='b', width=5, align='center')
    plt.show()


using_cumulative_histogram_equalization()
