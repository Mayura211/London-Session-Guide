from PIL import Image, ImageDraw
im = Image.new("RGBA", (256,256), (0,0,0,0))
d = ImageDraw.Draw(im)
d.rounded_rectangle((8,8,248,248), radius=52, fill="#19354b")
d.rounded_rectangle((18,18,238,238), radius=44, outline="#527b99", width=3)
for x,y1,y2,top,bottom,color in [(58,123,208,148,184,"#80b5da"),(104,91,175,111,154,"#70c8b5"),(150,102,163,118,146,"#80b5da"),(196,42,130,64,110,"#70c8b5")]:
    d.line((x,y1,x,y2),fill=color,width=6)
    d.rounded_rectangle((x-12,top,x+12,bottom),radius=4,fill=color)
im.save("icon.ico", sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
