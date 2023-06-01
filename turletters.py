import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	    pass
    elif letter == "C":
	    pass
    elif letter == "D":
	    pass
    elif letter == "E":
	    pass
    elif letter == "F":
	    pass
    elif letter == "G":
	    pass		
    elif letter == "H":
	    pass
    elif letter == "I":
	    pass
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	tur.setheading(0)
        tur.pd()
        tur.circle(50)
        tur.pu()
        tur.left(90)
        tur.fd(120)
        tur.right(90)
        tur.fd(60)
        tur.pu()
    elif letter == "P":
	    tur.setheading(0)
        tur.pd()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.forward(30)
        tur.right(180)
        tur.forward(30)
        tur.right(90)
        tur.circle(-10, 180)
        tur.pu()
        tur.right(180)
        tur.forward(20)
        tur.left(90)
        tur.forward(25)
        tur.right(90)
        tur.pu()		
    elif letter == "Q":
	tur.setheading(0)
        tur.pd()
        tur.circle(50)
        tur.pu()
        tur.left(45)
        tur.fd(30)
        tur.pd()
        tur.right(75)
        tur.fd(40)
        tur.pu()
        tur.left(120)
        tur.fd(140)
        tur.right(90)
    elif letter == "R":
	tur.setheading(0)
        tur.pd()
        tur.left(90)
        tur.fd(100)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.left(135)
        tur.fd(75)
        tur.bk(75)
        tur.left(135)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.pu()
    elif letter == "S":
	tur.setheading(0)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(50)
        tur.left(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(50)
        tur.pu()
    elif letter == "T":
	tur.setheading(0)
        tur.pd()
        tur.left(90)
        tur.fd(50)
        tur.left(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(40)
        tur.pu()
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
