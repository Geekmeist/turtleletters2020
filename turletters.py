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
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(50)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)   
    elif letter == "V":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.left(16.69924423)
        tur.fd(52.2015325)
        tur.left((90 - 16.69924423) * 2)
        tur.fd(52.2015325)
        tur.pu()
        tur.right(73.300755771)
        tur.fd(5)
        tur.left(90)
        tur.fd(5)
    elif letter == "W":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(50)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
            
    elif letter == "X":
        tur.setheading(0)
        tur.pu()
        tur.right(90)
        tur.fd(5)
        tur.left(90)
        tur.fd(5)
        tur.right(59.03624347)
        tur.pd()
        tur.fd(58.30951895)
        tur.setheading(90)
        tur.pu()
        tur.fd(50)
        tur.left(149.0362435)
        tur.pd()
        tur.fd(58.30951895)
        tur.pu()
        tur.setheading(0)
        tur.fd(35)
        tur.left(90)
        tur.fd(55)
    elif letter == "Y":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(15)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(15)
        tur.left(180)
        tur.fd(15)
        tur.right(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(35)
        tur.pu()
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(55)
            
    elif letter == "Z":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.setheading(0)
        tur.fd(30)
        tur.right(120.9637565)
        tur.fd(58.30951895)
        tur.left(120.9637565)
        tur.fd(30)
        tur.pu()
        tur.fd(5)
        tur.left(90)
        tur.fd(55)
                                    
    
        
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
    turtleLetter("U",tur)
    turtleLetter("V",tur)
    turtleLetter("W",tur)
    turtleLetter("X",tur)
    turtleLetter("Y",tur)
    turtleLetter("Z",tur)
    window.exitonclick()
