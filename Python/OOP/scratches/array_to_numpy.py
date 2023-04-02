import numpy as np
from PIL import Image

# Create a 3d numpy array of zeros, replace zeros (black pixels) with yellow pixels
data = np.zeros((5,4,3), dtype=np.uint8)
data[:] = [255, 255, 0]
print(data)
img = Image.fromarray(data, 'RGB')
img.save('my.png')