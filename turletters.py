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
        tur.fd(50)
        tur.right(180)
        tur.fd(50)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(50)
        tur.right(180)
        tur.fd(25)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(50)
        tur.right(180)
        tur.fd(25)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "C":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        #fixes
        tur.left(90)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "D":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        for i in range(0,2):
            tur.fd(50)
            tur.left(90)
            tur.fd(30)
            tur.left(90)
        tur.pu()
        tur.left(90)
        tur.fd(35)
        tur.left(90)
        tur.fd(5)
            
    elif letter == "E":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.fd(5)
        tur.left(90)
        tur.fd(5)
    elif letter == "F":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.right(180)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.pu()
        tur.fd(5)
        tur.left(90)
        tur.fd(5)
    elif letter == "G":
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
        tur.fd(25)
        tur.left(90)
        tur.fd(15)
        tur.pu()
        tur.right(90)
        tur.fd(25)
        tur.left(90)
        tur.fd(15)
        tur.pd()
        tur.right(180)
        tur.fd(30)
        tur.pu()
        tur.fd(5)
        tur.left(90)
        tur.fd(5)
    elif letter == "H":
	      tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(50)
        tur.right(180)
        tur.fd(25)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(25)
        tur.right(180)
        tur.fd(50)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "I": #wesstart
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.left(90)
        tur.pd()
        tur.speed(50)
        tur.fd(15)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(15)
        tur.right(180)
        tur.fd(30)
        tur.left(180)
        tur.fd(15)
        tur.right(90)
        tur.fd(50)
        tur.right(90)
        tur.fd(15)
        tur.pu()
        tur.left(90)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "J":
	      tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.left(90)
        tur.pd()
        tur.fd(30)
        tur.left(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(47)
        tur.right(45)
        tur.fd(5)
        tur.right(45)
        tur.fd(10)
        tur.right(45)
        tur.fd(7)
        tur.pu()
        tur.right(180)
        tur.fd(7)
        tur.left(45)
        tur.fd(10)
        tur.left(45)
        tur.fd(5)
        tur.left(45)
        tur.fd(47)
        tur.right(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(5)
        tur.right(90)
    elif letter == "K":
	      tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.left(90)
        tur.pd()
        tur.right(90)
        tur.fd(50)
        tur.right(180)
        tur.fd(25)
        tur.right(45)
        tur.fd(35)
        tur.right(180)
        tur.fd(35)
        tur.left(90)
        tur.fd(35)
        tur.left(180)
        tur.fd(35)
        tur.right(90)
        tur.fd(35)
        tur.pu()
        tur.left(45)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "L":
	      tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.left(90)
        tur.pd()
        tur.right(90)
        tur.fd(50)
        tur.left(90)
        tur.fd(30)
        tur.pu()
        tur.left(90)
        tur.fd(50)
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "M":
	      tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.left(90)
        tur.pd()
        tur.right(90)
        tur.fd(50)
        tur.left(180)
        tur.fd(50)
        tur.right(90)
        tur.left(180)
        tur.left(107)
        tur.fd(52)
        tur.left(147)
        tur.fd(52)
        tur.right(164)
        tur.fd(50)
        tur.right(180)
        tur.fd(50)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
    elif letter == "N": #wesend
	      tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.left(90)
        tur.pd()
        tur.right(90)
        tur.fd(50)
        tur.right(180)
        tur.fd(50)
        tur.right(90)
        tur.left(180)
        tur.left(120)
        tur.fd(55)
        tur.left(150)
        tur.fd(50)
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
    turtleLetter("A", tur)
    turtleLetter("B", tur)
    turtleLetter("C", tur)
    turtleLetter("D", tur)
    turtleLetter("E", tur)
    turtleLetter("F", tur)
    turtleLetter("G", tur)
    turtleLetter("H", tur)
    turtleLetter("I", tur)
    turtleLetter("J", tur)
    turtleLetter("K", tur)
    turtleLetter("L", tur)
    turtleLetter("M", tur)
    turtleLetter("N", tur)
    window.exitonclick()
