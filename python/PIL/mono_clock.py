from tkinter import tix
from tkinter.constants import *
from PIL import Image,ImageFont,ImageDraw,ImageTk
import time,math

class Frame(tix.Frame):

    def __init__(self,master=None):
        tix.Frame.__init__(self,master)
        self.master.title('mono_clock')

        #テキスト表示
        self.la = tix.Label(self,  bg='white')
        self.la.pack()

        #画像表示
        secfile   = 'textures/sec.png'
        minfile   = 'textures/min.png'
        hourfile  = 'textures/hour.png'
        gearfile  = 'textures/gear.png'
        gear1file = 'textures/gear1.png'
        tempfile  = 'textures/temp.png'

        self.secimage = Image.open(secfile)
        self.minimage = Image.open(minfile)
        self.hourimage = Image.open(hourfile)
        self.gearimage = Image.open(gearfile)
        self.gear1image = Image.open(gear1file)
        self.tempimage = Image.open( tempfile)
        self.tempAngle = 0.0#テンプ(素早く回ってる奴)
        #キャンバスの追加
        self.can = tix.Canvas(master, width=256, height=256,bg='white')
        self.can.pack(expand = True, fill = BOTH)
        self.loop()
   
    #無限ループ
    def loop(self):
        second = self.getSec()  / 60.0 #秒針
        minute = self.getMin()  / 60.0 #分針 
        hour   = self.getHour() / 12.0 #時針

        self.secimg  = ImageTk.PhotoImage(self.secimage.rotate(second * -360.0))
        self.minimg  = ImageTk.PhotoImage(self.minimage.rotate(minute * -360.0))
        self.hourimg = ImageTk.PhotoImage(self.hourimage.rotate(hour * -360.0))

        self.gearimg = ImageTk.PhotoImage(self.gearimage.rotate(second * -360.0))
        self.gear1img = ImageTk.PhotoImage(self.gear1image.rotate(minute * 360.0))
        self.tempAngle +=1.0
        self.tempimg = ImageTk.PhotoImage(self.tempimage.rotate(math.cos( self.tempAngle ) * 180.0 / 3.14))
        
        self.gear  = self.can.create_image(90, 128, anchor=CENTER, image=self.gearimg)
        self.gear1  = self.can.create_image(128, 128, anchor=CENTER, image=self.gear1img)
        self.temp  = self.can.create_image(180, 128, anchor=CENTER, image=self.tempimg)
        self.hour  = self.can.create_image(128, 128, anchor=CENTER, image=self.hourimg)
        self.mint  = self.can.create_image(128, 128, anchor=CENTER, image=self.minimg)
        self.sec   = self.can.create_image(128, 128, anchor=CENTER, image=self.secimg)
        #テキストの更新
        tex = self.getTimer()
        if time.strftime("%m") == 2 and time.strftime("%d") == 9:
            tex = "Happy BirthDay!!!"
        self.la.configure(text = tex)
        #時間更新 
        self.can.after(100, self.loop)

    #時刻取得
    def getTimer(self):
        return time.strftime("%Y/%m/%d (%a) %H:%M:%S", time.localtime())

    def getSec(self):
        return float(time.strftime("%S"))

    def getMin(self):
        return float(time.strftime("%M")) + self.getSec() /60.0  

    def getHour(self):
        return float(time.strftime("%I")) + self.getMin() / 60.0

if __name__ == '__main__':
     a = Frame()
     a.pack()
     a.mainloop()
