from tkinter import *
import random
import time
tk=Tk()
tk.title("PONG")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,   width=1000, height=500, bd=0, highlightthickness=0,bg="#292d33")
canvas.create_line(500,0,500,500,fill='#a4b9bf')
canvas.pack()
tk.update()

class Ball :
    def __init__(self,canvas,paddle1,paddle2,color):
        self.canvas = canvas
        self.paddle1=paddle1
        self.paddle2=paddle2
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id , 500, 250)
        start=[-3,-2,-1,0,2,3]
        random.shuffle(start)
        self.x=2
        self.y=start[0]
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        
        
        
    def hit_paddle1(self,pos):
        paddle1_pos=self.canvas.coords(self.paddle1.id)
        if pos[3]>=paddle1_pos[1] and pos[1]<= paddle1_pos[3]:            # hits the paddle area
            if pos[0]>=paddle1_pos[0] and pos[0]<=paddle1_pos[2]:
                return True
            return False
    
    def hit_paddle2(self,pos):
        paddle2_pos=self.canvas.coords(self.paddle2.id)
        if pos[3]>=paddle2_pos[1] and pos[1]<= paddle2_pos[3]:            # hits the paddle area
            if pos[2]>=paddle2_pos[0] and pos[2]<=paddle2_pos[2]:
                return True
            return False
    
    def draw(self):
        
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        
        print(pos)
        if pos[0]<=0:
            
            self.hit_leftside=True
            canvas.create_text(500,250,text='GAME OVER',fill='#6371cf')
        if pos[2]>=self.canvas_width:
            
            self.hit_rightside=True
            canvas.create_text(500,250,text='GAME OVER',fill='#6371cf')
        if pos[1]<=0:                                                       #drawing th ball in realtime
            self.y=2
        if pos[3]>=self.canvas_height:
            self.y=-2
        
        
        if self.hit_paddle1(pos)==True:#ball hitting tha paddle
            self.x=3 
               
        if self.hit_paddle2(pos)==True:#ball hitting tha paddle
            self.x=-3
            
            
class Paddle1:
        
    def __init__(self,canvas,color):
        
        self.canvas=canvas
        self.id= canvas.create_rectangle(0,0,10,100, fill=color)
        self.canvas.move(self.id,0,250) 
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down) 
        
    def draw(self):
        
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
            
    def turn_up(self,event):
        
        self.y=-3
        
    def turn_down(self,event):
        
        self.y=3

    
class Paddle2:
        
    def __init__(self,canvas,color):
        
        self.canvas=canvas
        self.id= canvas.create_rectangle(0,0,10,100, fill=color)
        self.canvas.move(self.id,990,250) 
        self.y=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-W>',self.turn_up1)
        self.canvas.bind_all('<KeyPress-S>',self.turn_down1) 
        self.canvas.bind_all('<KeyPress-w>',self.turn_up2)
        self.canvas.bind_all('<KeyPress-s>',self.turn_down2) 
    def draw(self):
        
        self.canvas.move(self.id,0,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.y=-3
            
    def turn_up1(self,event):
        
        self.y=-3
        
    def turn_down1(self,event):
        
        self.y=3

    def turn_up2(self,event):
        
        self.y=-3
        
    def turn_down2(self,event):
        
        self.y=3





paddle1=Paddle1(canvas,'#e37da9')
paddle2=Paddle2(canvas,'#e37da9')
ball=Ball(canvas,paddle1,paddle2, '#74b59a') 




while 1:
    ball.draw()
    paddle1.draw()
    paddle2.draw()
       
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)    