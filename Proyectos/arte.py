#este programa tiene la intención de familiarizar a los alumnos con una sintaxis más compleja; la utilización de módulos; 
#operadores lógicos menos comunes; built-in functiones y loops


import turtle
turtle.bgcolor('black')

t = turtle.Turtle()
colors = ['red', 'dark red']

for number in range(400):
  t.forward(number+1)
  t.right(89)
  t.pencolor(colors[number%2])
turtle.done()
