import json,shutil,os

#LionHack 2022 
#NFT Refraction Project
#c/o Peter Bowman-Davis, Jordan Bowman-Davis, Zaid Fattah, Felix Law
#counterpart to the ImageGen program, generates the relevant metadata for the test images


#Iterates over the range of # of colors for each pixel
colorAlphabetical=["R","G","B","Y"]
i=0
for Pixel1 in range(len(colorAlphabetical)):
    for Pixel2 in range(len(colorAlphabetical)):
        for Pixel3 in range(len(colorAlphabetical)):
            for Pixel4 in range(len(colorAlphabetical)):

                ZeroZero=Pixel1
                OneZero=Pixel2
                ZeroOne=Pixel3
                OneOne=Pixel4

                #Creates the name of the NFT based upon its composition (0,0),(0,1),(1,0),(1,1) which will serve as an ID later on
                name=colorAlphabetical[Pixel1]+colorAlphabetical[Pixel2]+colorAlphabetical[Pixel3]+colorAlphabetical[Pixel4]
                
                #Creates the JSON-compatible dictionary, with coordinate-color pairs as attributes to later be refracted  
                ExportDict ={
                    "description": "Custom, highely prestigious 4x4 blocks.", 
                    "image": "https://storage.googleapis.com/opensea-prod.appspot.com/puffs/3.png", 
                    "name": name,

                    "Attributes": {
                        "ZeroZero": colorAlphabetical[Pixel1],
                        "OneZero": colorAlphabetical[Pixel2],
                        "ZeroOne": colorAlphabetical[Pixel3],
                        "OneOne": colorAlphabetical[Pixel4]
                    },
                }
                i=i+1

                #Saves the output file as a JSON with numerical values equal to that of the ImageGen program
                out_file = open(str(i)+".json", "w")
                json.dump(ExportDict, out_file, indent = 6)
                out_file.close()
#Tests if directory exists. If not, make it exists
path=os.getcwd()
if not os.path.exists(path+"/ImgMetadata"):
  # Create a new directory because it does not exist 
  os.makedirs(path+"/ImgMetadata")

#Moves files
for n in range(256):
    shutil.move("./"+str(n+1)+".json", "./ImgMetadata/"+str(n+1)+".json")
    