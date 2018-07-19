#coding=utf-8
from Tkinter import *


class GAME():#游戏类
    z_height=30
    now,step,over,qipu=0,0,-1,{}
    C,Z=0,0
    def __init__(self,dw,g_height,g_width):
        self.dw,self.g_height,self.g_width=dw,g_height,g_width
        self.height,self.width=self.g_height*self.dw+self.z_height,self.g_width*self.dw
        self.window = Tk()
        self.window.title(u'五子棋')
        self.center_window()
        self.window.bind('<Key>', self.key)
        self.qipan()
        self.zhuangtai()
        self.window.mainloop()

    def center_window(self):
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws/2) - (self.width/2)
        y = (hs/2) - (self.height/2)
        self.window.minsize(self.width,self.height)
        self.window.maxsize(self.width,self.height)
        self.window.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y))


    def click(self,e):
        x,y=e.x/self.dw,(e.y-self.z_height)/self.dw
        if x<0 or y<0 or x>=self.g_width or y>=self.g_height or str(x)+"-"+str(y) in self.qipu or self.over!=-1:
            return
        self.qipu[str(x)+"-"+str(y)]=self.now
        self.over=self.is_win(x,y)
        x,y=x*self.dw+self.dw/2,y*self.dw+self.dw/2
        color="white" if self.now==1 else "black"
        self.C.create_oval(x,y+self.z_height,x,y+self.z_height,width=self.dw-self.dw/8,outline=color)
        self.now=0 if self.now==1 else 1
        self.step+=1
        self.zhuangtai()


    def is_win(self,x,y):
        n=self.qipu[str(x)+"-"+str(y)]
        r=1
        #竖
        for j in xrange(2):
            for i in range(1,5):
                temp=y-i if j==0 else y+i
                if temp<0 or temp>=self.g_height or str(x)+"-"+str(temp) not in self.qipu:
                    break
                if self.qipu[str(x)+"-"+str(temp)]!=n:
                    break
                r+=1
        if r>=5:return n


        r=1
        #横
        for j in xrange(2):
            for i in range(1,5):
                temp=x-i if j==0 else x+i
                if temp<0 or temp>=self.g_width or str(temp)+"-"+str(y) not in self.qipu:
                    break
                if self.qipu[str(temp)+"-"+str(y)]!=n:
                    break
                r+=1
        if r>=5:
            return n


        r=1
        #左斜
        for j in xrange(2):
            for i in range(1,5):
                temp1=x-i if j==0 else x+i
                temp2=y-i if j==0 else y+i
                if temp1<0 or temp1>=self.g_width or temp2<0 or temp2>=self.g_height or str(temp1)+"-"+str(temp2) not in self.qipu:
                    break
                if self.qipu[str(temp1)+"-"+str(temp2)]!=n:
                    break
                r+=1
        if r>=5:
            return n


        r=1
        #右斜
        for j in xrange(2):
            for i in range(1,5):
                temp1=x+i if j==0 else x-i
                temp2=y-i if j==0 else y+i
                if temp1<0 or temp1>=self.g_width or temp2<0 or temp2>=self.g_height or str(temp1)+"-"+str(temp2) not in self.qipu:
                    break
                if self.qipu[str(temp1)+"-"+str(temp2)]!=n:
                    break
                r+=1
        if r>=5:
            return n
        return -1


    def key(self,e):
        if e.keycode==71 and self.over!=-1:
            self.now,self.step,self.over,self.qipu=0,0,-1,{}
            self.qipan(True)
            self.zhuangtai()



    def qipan(self,z=False):
        if z==False:
            self.C = Canvas(self.window, bg="#009999", height=self.height, width=self.width)
        else:
            self.C.delete("all")
        for i in xrange(self.g_width+1):
            self.C.create_line((i-1)*self.dw,0+self.z_height,(i-1)*self.dw,self.height,fill="#333333")
        for i in xrange(self.g_height+1):
            self.C.create_line(0,(i-1)*self.dw+self.z_height,self.width,(i-1)*self.dw+self.z_height,fill="#333333")
        if z==False:
            self.C.bind("<Button-1>", self.click)
            self.C.pack()


    def zhuangtai(self):
        text=u"游戏状态:"
        if self.step==0:
            text+=u" 游戏开始,黑棋先走"
        elif self.over!=-1:
            text+=u" 游戏结束 "+(u"黑棋" if self.over==0 else u"白棋")+u"胜利! 按F5重新开始"
        elif self.step==self.g_width*self.g_height:
            text+=u" 游戏结束 和棋! 按F5重新开始"
        else:
            text+=u" 当前"+(u"黑棋" if self.now==0 else u"白棋")+u"走棋 总共"+str(self.step)+u"步"
        self.Z = Label( self.C, text=" "*len(text)*4+text,justify="right",width=self.width*2)
        self.Z.place(anchor="n",height=self.z_height)



if __name__ == '__main__':
    game=GAME(33,22,33) #这三个数字分别代表个棋盘每个小块的长度，棋盘高多少个小块，宽多少个小块
