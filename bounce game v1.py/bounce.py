from tkinter import *
import time
import random
tk=Tk()

tk.title("Bounce")
tk.resizable(0,0)#wont change size
tk.wm_attributes("-topmost",1)#front of all the windows
canvas=Canvas(tk,   width=500, height=500, bd=0, highlightthickness=0,bg="#292d33")#bd=border,and highlightthickness border thickness
canvas.pack()
tk.update()


class Ball:
    
    def __init__(self , canvas ,paddle, color):
        
        self.canvas = canvas
        self.paddle=paddle
        self.id = canvas.create_oval(10,10,25,25, fill = color)
        self.canvas.move(self.id , 245, 100)
        start=[-3,-2,-1,0,2,3]
        random.shuffle(start)
        self.x=start[0]
        self.y=-3
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
    
    
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<= paddle_pos[2]:            # hits the paddle area
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
            return False
        
        
    def draw(self):
        
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        
        print(pos)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
            canvas.create_text(245,100,text='GAME OVER')
        if pos[0]<=0:                                                       #drawing th ball in realtime
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        
        
        if self.hit_paddle(pos)==True:#ball hitting tha paddle
            self.y=-3    

            

class Paddle:
    
    def __init__(self,canvas,color):
        
        self.canvas=canvas
        self.id= canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move(self.id,245,300) 
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right) 
        
    def draw(self):
        
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
            
    def turn_left(self,event):
        
        self.x=-3
        
    def turn_right(self,event):
        
        self.x=3





    
paddle=Paddle(canvas,'#e37da9')
ball=Ball(canvas,paddle, '#74b59a') 


while 1:
    if ball.hit_bottom==False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)                                            #run every 0.01 second
    