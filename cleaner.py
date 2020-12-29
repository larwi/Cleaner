import sys
import turtle
import time
from random import randint
import ruta
wn = turtle.Screen()
wn.setup(250, 250)
if (len(sys.argv)>=2):
	ruta.pel=int(sys.argv[1])
ruta.rita_rum()

def go():
	ruta.fram()
	ruta.vrid_h()
	ruta.fram()
	ruta.vrid_v()
	for j in range(2):
		for i in range(7):
			ruta.fram()
			if(ruta.check_color() == 2):
				ruta.clean()
		ruta.vrid_v()
		ruta.fram()
		ruta.vrid_v()

def q():
	wn.bye() 

wn.onkey(go, "space")
wn.onkey(q, "q")
wn.listen()
wn.mainloop()