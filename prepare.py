import os

fileinput = open("templates.txt", "r")                  #Load input
fileinput = fileinput.read().splitlines()

text = "cd C:\Program Files\ImageMagick-7.1.0-Q16-HDRI"

templates = []

text = ""
unite = ""
i=0

focus = int(input("focus:"))
width = int(input("width:"))
height = int(input("height:"))


for x in fileinput:
    x = x.rsplit("\t")
    size = x[1] + "x" + x[2]
    
    scaling_w = float(x[1])/width
    scaling_h = float(x[2])/height
    
    scaling = max (scaling_w, scaling_h)

    offset_v = 0
    
    if (x[4]=="full"):
        offset_v = 0
        if x[3] == "width":
            offset_v = (float(x[2]) - float(x[1])) /2
        
        command = "magick convert -background none -density 300 -resize " + size + " -extent " + size + "+0+" + str(offset_v) + " -gravity center C:/Users/mwessel/Documents/Merch/input.svg C:/Users/mwessel/Documents/Merch/" + x[0] + ".png"

    if (x[4]=="duffle"):
        offset = str( (int (x[1]) - int(x[3]) )/2 )
        command = "magick convert -background none  -density 300 -resize " + x[3] + "x" + x[2] + "^^ -extent " + size + "+" + offset + " -gravity center -rotate 90 C:/Users/mwessel/Documents/Merch/input.svg C:/Users/mwessel/Documents/Merch/" + x[0] + ".png"

    if (x[4]=="crop"):
        offset_h = (focus - width/2) * scaling_h
   
        if focus == 0:
            offset_h = 0
 
        max_offset_h = -( width * scaling - float(x[1]))/2

        offsets = [offset_h, max_offset_h, -max_offset_h]
        offsets.sort()
        offset_h =  offsets[1]
        offset_h = round(offset_h,0)
        
        command = f"magick convert -background none -density 300 -resize {size}^^ -extent {size}+{offset_h} -gravity center {x[3]} C:/Users/mwessel/Documents/Merch/input.svg C:/Users/mwessel/Documents/Merch/{x[0]}.png"

    if (x[4]=="uncropped"):
        command = f"magick convert -background none -density 300 -resize {size}^^ -gravity center C:/Users/mwessel/Documents/Merch/input.svg C:/Users/mwessel/Documents/Merch/{x[0]}.png"

    if (x[4]=="border"):
        border = str(int(x[1])-2*int(x[3])) + "x" + str(int(x[2])-2*int(x[3]))
        print (border)
        size = x[1] + "x" + x[2]
        
        command = f"magick convert -background white -density 300 -resize {border} -extent {size} -gravity center C:/Users/mwessel/Documents/Merch/input.svg C:/Users/mwessel/Documents/Merch/{x[0]}.png"

    text = text + "\n" + command


text = text + "\npause"

with open(r'resize.bat', "w") as resize:
    resize.write((text))   