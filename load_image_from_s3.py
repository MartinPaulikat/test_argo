#import PIL
from PIL import Image
import sys

#the file path is given as a argument to this script
file_path = sys.argv[1]
#the save path is given as a argument to this script
save_path = sys.argv[2]

#open the image
img = Image.open(file_path)
#save the image in the save path
img.save(save_path)
print("Image saved in " + save_path, file=sys.stdout)