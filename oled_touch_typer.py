from time import sleep
from machine import Pin, I2C ,TouchPad
from ssd1306 import SSD1306_I2C 

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) 
oled = SSD1306_I2C(128, 64, i2c, addr=0x3C)

left = TouchPad(Pin(4))
right = TouchPad(Pin(15))
up = TouchPad(Pin(13))
okb = TouchPad(Pin(14))

position=0
xx,yy=0,0
clear=0

def get_val(var):
    try:
        val=var.read()
    except:
        val=0
    if val<50:
        val=0
    return val

def writ(pos,o,x,y,era):
    if era==1:
        oled.fill(0)
        era=0
        return 0,0,era,0
    stri='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    oled.text(stri[pos],x,y)
    if o==0:
        oled.show()
        x+=10
    return x,y,era,pos

while True:
    l,r,u,ok=get_val(left),get_val(right),get_val(up),get_val(okb)
#     print(l,r,ok)
    if l==0:
        position-=1
    if r==0:
        position+=1
    if u==0:
        clear=1
    if position>25:
        position=0
    if position<-25:
        position=0
    print(position)
    if xx>=120:
        xx=0
        yy+=10
    xx,yy,clear,position=writ(position,ok,xx,yy,clear)
    sleep(0.2)
# The following codes should be tested using the REPL.
# #1. To print a string:  
# oled.text('Hello world', 0, 0) 
# #2. To display all the commands in queue:     
# oled.show() 
# #3. Now to clear the oled display:  
# oled.fill(0) 
# oled.show() 
# #4. You may also use the invert function to invert the display.  
# oled.invert(1) 
# #5.To display a single pixel.  
# oled.pixel(10,20,1) 
# oled.show() 
# #6. To display a horizontal line  
# oled.hline(30,40,10,1) 
# oled.show() 
# #7. To display a vertical line  
# oled.vline(30,45,5,1) 
# oled.show() 
# #8. While hline and vline is quite useful, there is another function that is more flexible to use which is the line function.  
# oled.line(0,50,10,50,1) 
# oled.show() 
# #9.We may also be able to print a rectangle.  
# oled.rect(10,60,10,5,1) 
# oled.show() 
# #10. Or we may also print a filled rectangle:  
# oled.fill_rect(10,70,10,5,1) 
# oled.show()