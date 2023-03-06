#este programa tiene la intención de familiarizar a los alumnos con una sintaxis más compleja; la utilización de módulos; 
#operadores lógicos menos comunes; built-in functiones y loops

# importing turtle module
import turtle

# number of sides
n = 10
pen = turtle.Turtle()

for i in range(n):
	pen.forward(i * 10)	
	pen.right(144)

turtle.done()
