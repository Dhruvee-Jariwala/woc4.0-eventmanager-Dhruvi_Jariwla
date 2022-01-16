import turtle

def pattern(x,y,r,g,b):
    a = turtle.Pen()
    a.speed(0)
    a.up()
    a.goto(x,y)
    a.pd()
    a.pensize(2)
    turtle.colormode(255)
    for i in range(30,50):
        a.left(18)
        a.pencolor(r*i*5,g*i*5,b*i*5)
        a.circle(50)

if __name__ == '__main__':
    pattern(0, 0, 0, 0, 1)  #blue mid
    pattern(150,150,0,1,1)  #right up
    pattern(0, 300, 0, 1, 1)    #up mid
    pattern(-150,150,0,1,1)     #left up
    pattern(-300, 0, 0, 1, 1)      #left mid
    pattern(-150, -150, 0,1,1)    #left down
    pattern(0, -300, 0, 1, 1)       #mid down
    pattern(150, -150, 0,1,1)     #right down
    pattern(300, 0, 0, 1, 1)     #right mid

    pattern(350, 200, 1, 0, 0)     #right up first
    pattern(200, 350, 1, 0, 0)  # right up second
    pattern(-200, 350, 1, 0, 0)  # left up second
    pattern(-350, 200, 1, 0, 0)  # left up first
    pattern(-500, 0, 1, 0, 0)  # left mid last
    pattern(-350, -200, 1, 0, 0)  # left down first
    pattern(-200, -350, 1, 0, 0)  # left down second
    pattern(200, -350, 1, 0, 0)  # right down second
    pattern(350, -200, 1, 0, 0)  # right down first
    pattern(500, 0, 1, 0, 0)  # left mid last
    turtle.bgcolor(0,0,0)
    turtle.done()


