from webptools import webplib  as webp
from PIL import Image
import os

def Webp_TO_Gif():
    path = "C:/Users/CHENG_CL/Desktop/Weibo"
    file_list = os.listdir(path + "_Webp")

    t = None
    for file in file_list:
        old_Name = path + "_Webp/" + file
        print(old_Name)
        if os.path.exists(old_Name):
            front, behind = file.split(".", 1)
        else:
            print("No such fille: %s", old_Name)

        new_Name = path + "_Gif/" + front
        # print(new_Name + ".png")
        # print(webp.dwebp(old_Name, new_Name + ".png", "-o"))

        #https://github.com/mougua/webp2gif/blob/master/webp.py
        im = Image.open(new_Name + ".png")
        # Get the alpha band
        alpha = im.split()[3]

        # Convert the image into P mode but only use 255 colors in the palette out of 256
        im = im.convert('RGB').convert('P', palette = Image.ADAPTIVE, colors=255)

        # Set all pixel values below 128 to 255,
        # and the rest to 0
        mask = Image.eval(alpha, lambda a: 255 if a <= 180 else 0)

        # Paste the color of index 255 and use alpha as a mask
        im.paste(255, mask)
        # The transparency index is 255
        im.save(new_Name + ".gif", transparency=255)
        if os.path.exists(new_Name + ".png"):
            os.remove(new_Name + ".png")
        else:
            print("No such file:%s", old_Name)

Webp_TO_Gif()