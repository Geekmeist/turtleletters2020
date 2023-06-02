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
            pass
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
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.forward(50)
        tur.left(90)
        tur.forward(30)
        tur.left(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(30)
        tur.pu()
        tur.right(180)
        tur.forward(35)
    elif letter == "P":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.forward(50)
        tur.pu()
        tur.left(180)
        tur.forward(50)
        tur.pd()
        tur.right(90)
        tur.forward(30)
        tur.right(90)
        tur.forward(25)
        tur.right(90)
        tur.forward(30)
        tur.pu()
        tur.right(90)
        tur.forward(25)
        tur.right(90)
        tur.forward(35)
    elif letter == "Q":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.forward(50)
        tur.left(90)
        tur.forward(30)
        tur.left(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(30)
        tur.pu()
        tur.left(90)
        tur.forward(40)
        tur.left(90)
        tur.forward(20)
        tur.right(90)
        tur.pd()
        tur.forward(15)
        tur.pu()
        tur.right(180)
        tur.forward(55)
        tur.right(90)
        tur.forward(15)
        
    elif letter == "R":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.pd()
        tur.forward(50)
        tur.pu()
        tur.left(180)
        tur.forward(50)
        tur.pd()
        tur.right(90)
        tur.forward(30)
        tur.right(90)
        tur.forward(25)
        tur.right(90)
        tur.forward(30)
        tur.pu()
        tur.right(180)
        tur.forward(10)
        tur.right(90)
        tur.pd()
        tur.forward(25)
        tur.pu()
        tur.right(180)
        tur.forward(50)
        tur.right(90)
        tur.forward(25)
    elif letter == "S":
        tur.setheading(0)
        tur.pu()
        tur.fd(35)
        tur.left(180)
        tur.pd()
        tur.forward(30)
        tur.left(90)
        tur.forward(25)
        tur.left(90)
        tur.forward(30)
        tur.right(90)
        tur.forward(25)
        tur.right(90)
        tur.forward(30)
        tur.pu()
        tur.right(90)
        tur.forward(50)
        tur.right(90)
        tur.forward(35)
        
    elif letter == "T":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.pd()
        tur.forward(30)
        tur.pu()
        tur.right(180)
        tur.forward(15)
        tur.left(90)
        tur.pd()
        tur.forward(50)
        tur.pu()
        tur.right(180)
        tur.forward(50)
        tur.right(90)
        tur.forward(20)
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
    tur.speed(999)
    #turtleLetter("box",tur)
    turtleLetter("O",tur)
    turtleLetter("P",tur)
    turtleLetter("Q",tur)
    turtleLetter("R",tur)
    turtleLetter("S",tur)
    turtleLetter("T",tur)

    
    window.exitonclick()
