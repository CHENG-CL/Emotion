from webptools import webplib  as webp
from PIL import Image
import imageio
import os

def Webp_TO_Gif():
    path = "C:/Users/cheng_cl/Desktop/Weibo"
    if "Weibo" in path:
        Format_Of_File = "webp"
    elif "Tieba" in path:
        Format_Of_File = "png"
    file_list = os.listdir(path + "_" + Format_Of_File)

    for file in file_list:
        old_Name = path + "_" + Format_Of_File + "/" + file
        if os.path.exists(old_Name):
            front, behind = file.split(".", 1)
        else:
            print("No such fille: %s", old_Name)

        new_Name = path + "_Gif/" + front

        # convert the webp to png
        if "Weibo" in new_Name:
            # print(new_Name + ".png")
            # print(webp.dwebp(old_Name, new_Name + ".png", "-o"))
            webp.dwebp(old_Name, new_Name + ".png", "-o")

        print(new_Name + ".png")
        # https://github.com/mougua/webp2gif/blob/master/webp.py
        im = Image.open(new_Name + ".png")

        # convert the channel to "RGBA"
        if len(im.split()) != 4:
            im = im.convert("RGBA")

        # Get the alpha band
        alpha = im.split()[3]
        # Convert the image into P mode but only use 255 colors in the palette out of 256
        im = im.convert('RGB').convert('P', palette = Image.ADAPTIVE, colors=255)

        # Set all pixel values below 128 to 255,
        # and the rest to 0
        # 边缘阴影调节
        mask = Image.eval(alpha, lambda a: 255 if a <= 200 else 0)

        # Paste the color of index 255 and use alpha as a mask
        im.paste(256, mask)
        # The transparency index is 255
        print(new_Name + ".gif")
        im.save(new_Name + ".gif", transparency=255)
        # delete the png image
        if os.path.exists(new_Name + ".png"):
            os.remove(new_Name + ".png")
        else:
            print("No such file:%s", old_Name)

Webp_TO_Gif()