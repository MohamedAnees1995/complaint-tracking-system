pip install imageio


import imageio as iio

img = iio.imread("images.jpg")

iio.imwrite("g4g.jpg", img)