from PIL import Image, ImageDraw
import math
S=768
im=Image.new("RGBA",(S,S),(0,0,0,0))
mask=Image.new("L",(S,S),0)
ImageDraw.Draw(mask).rounded_rectangle((18,18,750,750),radius=162,fill=255)
bg=Image.new("RGBA",(S,S))
p=bg.load()
for y in range(S):
    for x in range(S):
        t=(x+y)/(2*S)
        p[x,y]=(int(26-14*t),int(86-57*t),int(123-75*t),255)
im.paste(bg,(0,0),mask)
d=ImageDraw.Draw(im)
d.rounded_rectangle((25,25,743,743),radius=155,outline="#6596ad",width=5)
# London clock motif, behind the trading candles.
d.ellipse((116,100,652,636),outline="#527c91",width=9)
for i in range(12):
    a=math.pi*i/6
    r=249
    d.line((384+math.sin(a)*r,368-math.cos(a)*r,384+math.sin(a)*(r-19),368-math.cos(a)*(r-19)),fill="#7296a8",width=7)
d.line((384,368,384,194),fill="#7296a8",width=10)
d.line((384,368,486,307),fill="#7296a8",width=10)
# High contrast ascending candlesticks.
for x,lo,hi,top,bottom,c in [(212,570,350,416,514,"#e7f4ff"),(326,516,284,345,449,"#5ce1c1"),(440,455,241,301,395,"#e7f4ff"),(554,354,156,213,305,"#5ce1c1")]:
    d.line((x,hi,x,lo),fill=c,width=14)
    d.rounded_rectangle((x-35,top,x+35,bottom),radius=12,fill=c)
im=im.resize((256,256),Image.Resampling.LANCZOS)
im.save("icon.ico",sizes=[(16,16),(24,24),(32,32),(48,48),(64,64),(128,128),(256,256)])
