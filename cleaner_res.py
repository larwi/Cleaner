import turtle
import time
from random import randint
import ruta
wn = turtle.Screen()
wn.setup(250, 250)
ruta.rita_rum()
	
def go():
	ruta.fram()
	ruta.vrid_h()
	ruta.fram()
	ruta.fram()
	ruta.vrid_v()
	for j in range(4):
		for i in range(7):
			ruta.fram()
			if ruta.check_color() == 2:
				ruta.clean()
		ruta.vrid_v()
		ruta.fram()
		if ruta.check_color() == 2:
			ruta.clean()
		ruta.vrid_v()
		for i in range(7):
			ruta.fram()
			if ruta.check_color() == 2:
				ruta.clean()
		ruta.vrid_h()
		ruta.fram()
		if ruta.check_color() == 2:
			ruta.clean()
		ruta.vrid_h()
	ruta.vrid_h()
	for i in range(6):
		ruta.fram()
	ruta.vrid_h()
	ruta.fram()

def q():
	wn.bye() 

wn.onkey(go, "space")
wn.onkey(q, "q")
wn.listen()
wn.mainloop()