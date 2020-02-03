import turtle
import math

def Timer_func():
    x,y = t.pos()
    if x<-300 or x>300: 
        t.right(180)
    t.forward(50)
    wn.ontimer(Timer_func,500)

size=800
turtle.setup(size,size)
wn=turtle.Screen()


m=turtle.Turtle()
e=turtle.Turtle()
t=turtle.Turtle()
def draw_blocks(x,height,width):    
    for i in range(2):
        x.begin_fill()
        x.left(90)
        x.forward(height)
        x.left(90)
        x.forward(width)
        x.end_fill()
        x.color("black","black")

k=turtle.Turtle()
k.pensize(20)
k.penup()
k.setposition(350,350)
k.pendown()
k.right(90)
k.forward(650)
k.right(90)
k.forward(700)
k.right(90)
k.forward(650)
k.right(90)
k.forward(700)


a=turtle.Turtle()
b=turtle.Turtle()
c=turtle.Turtle()

a.penup()
b.penup()
c.penup()

a.setposition(-150,100)
b.setposition(50,100)
c.setposition(250,100)

draw_blocks(a,20,150)
draw_blocks(b,20,150)
draw_blocks(c,20,150)

        
wn.bgcolor("light blue")

             
m.shape("turtle")
e.shape("turtle")
t.shape("turtle")

m.fillcolor("green")
e.fillcolor("yellow")
t.fillcolor("red")

m.penup()
e.penup()
t.penup()

t.setposition(-300,200)
e.setposition(0,200)
m.setposition (0,-250)
m.left(90)
  
def a():
    m.penup()
    m.forward(20)
def b():
        m.penup()
        m.right(90)
        m.forward(20)
        m.left(90)
        
        
def c():
        m.penup()
        m.left(90)  
        m.forward(20)
        m.right(90)


turtle.onkey(a,'Up')
x1,y1 = t.pos()

if x1>=-300 or x1<=300:
    
    turtle.onkey(b,"Right")
    
if x1>=-300 or x1<=300:
        
    turtle.onkey(c,"Left")




    
wn.ontimer(Timer_func,500)
wn.listen()    
wn.mainloop()


turtle.listen()
turtle.mainloop()

wn.exitonclick()