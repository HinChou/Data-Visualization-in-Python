# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 23:05:36 2017

@author: hinnc
"""

from PIL import Image, ImageDraw, ImageFont


img = Image.open(".\Xie_Emoji_meitu_2.jpg")
thug_life_text = Image.open(".\Thug-Life-Text_meitu_1.jpg")
#glasses = Image.open(".\Thug-Life-Glasses-3_meitu_5.png")
glasses = Image.open(".\Thug-Life-Glasses-3_meitu_3.jpg")
#hat = Image.open(".\Thug-Life-Hat-1_meitu_1.jpg")
fire = Image.open(".\Fire_meitu_2.jpg")
#gun = Image.open(".\Gun.jpg")

# Paste other images on the top of img
img.paste(thug_life_text, (150,0))
img.paste(glasses, (160,458))
img.paste(fire, (123,572))
#img.paste(gun,(150,450))
#img.paste(hat,(250,230))
img.show()

# Add sentences on the image
draw = ImageDraw.Draw(img)  
ttfront = ImageFont.truetype('simhei.ttf', 45) 
draw.text((50, 160), "我的内心毫无波动，甚至还想笑", fill=(0,0,0), font=ttfront) 
img.show()
img.save(".\Python_Emoji.jpg")
