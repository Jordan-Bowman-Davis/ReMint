#LionHack 2022 

#NFT Refraction Project -- Refract any NFT into principle components, reassemble into a new collection -- adopt your digital identity.

#c/o Peter Bowman-Davis, Jordan Bowman-Davis, Zaid Fattah, Felix Law

#Creates "NFT Ready" Permutations of an 4x4 image for testing using 4 colors (256 resulting .PNG images)

import PIL,shutil, os
from PIL import Image
 
# RGB mode and size 200x200

listOfImages=[] #Will later be the list of image pointers
colors=[(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0)] #Red, Green, Blue, Yellow
im = PIL.Image.new(mode = "RGB", size = (2, 2), color = (0, 0, 0)) #initialize blank image

#Iterates over the list of colors once for each pixel. 
for Pixel1 in range(len(colors)):
    for Pixel2 in range(len(colors)):
        for Pixel3 in range(len(colors)):
            for Pixel4 in range(len(colors)):
                
                #Changes pixel at appropriate location
                im.putpixel((0, 0), colors[Pixel1])
                im.putpixel((1, 0), colors[Pixel2])
                im.putpixel((0, 1), colors[Pixel3])
                im.putpixel((1, 1), colors[Pixel4])
                
                #appends the im pointer into the list and resets the im object
                listOfImages.append(im)
                im = PIL.Image.new(mode = "RGB", size = (2, 2), color = (0, 0, 0)) 

#Saves the image as a PNG with maximum quality/no subsampling (which causes issues at this small scale)
for i in range(len(listOfImages)):
    listOfImages[i].save(str(i+1)+"a"+".png",quality=100,subsampling=0)

#Tests if directory exists. If not, make it exists
path=os.getcwd()
if not os.path.exists(path+"/ImgMetadata"):
  # Create a new directory because it does not exist 
  os.makedirs(path+"/ImgMetadata")
  print("The new directory is created!")

# Moves files into the directory
for n in range(256):
    shutil.move("./"+str(n+1)+"a.png", "./ImgMetadata/"+str(n+1)+"a.png")