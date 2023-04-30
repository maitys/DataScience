import os
import numpy as np
from PIL import Image

# Create a 3d numpy array of zeros, replace zeros (black pixels) with yellow pixels
data = np.zeros((500,400,3), dtype=np.uint8) # 5,4,3 = 5 arrays of 4 rows of 3 columns
data[:] = [255, 255, 0]
img = Image.fromarray(data, 'RGB')

dir_path = os.path.dirname(os.path.realpath(__file__))
img.save(dir_path + '/my.png')

# Create a 3d numpy array of zeros, replace zeros (black pixels) with yellow pixels
data = np.zeros((500,400,3), dtype=np.uint8) # 5,4,3 = 5 arrays of 4 rows of 3 columns
data[1:300] = [255, 0, 0] # color = red
data[300:] = [0, 255, 0] # color = green
data[:, :200] = [0, 0, 255] # color = blue
data[100:300, 100:300] = [255, 255, 0] # color = yellow

img = Image.fromarray(data, 'RGB')
dir_path = os.path.dirname(os.path.realpath(__file__))
img.save(dir_path + '/my2.png')