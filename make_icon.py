from PIL import Image, ImageDraw
im = Image.new("RGBA", (256,256), "#245c89")
d = ImageDraw.Draw(im)
d.rounded_rectangle((10,10,245,245), radius=38, outline="#9bc9e8", width=5)
for y in (64,112,160,208):
    d.line((27,y,229,y), fill="#39739e", width=2)
for x,y1,y2,top,bottom,color in [(57,123,211,146,187,"#ffffff"),(104,91,175,111,154,"#8be3cd"),(151,102,163,118,146,"#ffffff"),(198,36,130,60,110,"#8be3cd")]:
    d.line((x,y1,x,y2),fill=color,width=7)
    d.rounded_rectangle((x-13,top,x+13,bottom),radius=3,fill=color)
im.save("icon.ico", sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
