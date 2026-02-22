import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    images.append(Image.open(arg))
images[0].save('costums.gif', save_all=True, append_images=images[1:], loop=0)