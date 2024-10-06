from turtle import*
 #we want to paint a house

#step 1 :draw a square
width(7)
color("purple")
forward(200)
left(90)


forward (200)
left(90)

forward(200)
left(90)


forward (200)
left(90)
#end of square

#drawing a door 

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#drawing a window
penup()

color("green")
goto(150, 90) 
begin_fill()

pendown()
right(150)

forward(70)

penup()

goto(175,90)

pendown()
forward(70)
penup()

goto(150,90)
begin_fill()
pendown()
right(90)
forward(30)
left(90)
forward(70) 
left(90)
forward(30)
end_fill()
penup()
goto(50,90)
begin_fill()
pendown()
forward(35)
right(90)
forward(70)
right(90) 
forward(35)
right(90)
forward(70) 
end_fill()
exitonclick()

