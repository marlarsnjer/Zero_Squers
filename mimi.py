import turtle as t
 
y=320
t.penup()
t.goto(-320,y)
t.pendown()
 
def white_square():
    for i in range(4):
        t.fd(80)
        t.rt(90)
def black_square():
    t.color("black","black")
    t.begin_fill()
    for i in range(4):
        t.fd(80)
        t.rt(90)
    t.end_fill()
   
for a in range(4):  
    for e in range(4): 
        white_square()
        t.fd(80)
        black_square()
        t.fd(80)
 
    y=y-80   
    t.penup()
    t.goto(-320,y)
    t.pendown()
 
    for e in range(4): 
        black_square()
        t.fd(80)
        white_square()
        t.fd(80)
       
    y=y-80   
    t.penup()
    t.goto(-320,y)
    t.pendown()