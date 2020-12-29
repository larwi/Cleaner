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
	steg = 0
	ruta.fram()
	if ruta.check_color() == 2:
		ruta.clean()
	while ruta.how_many() > 0:
		r = randint(0, 9)
		if r == 0 and ruta.kolla_k() != 9:
			ruta.vrid_v()
		elif r == 1 and ruta.kolla_k() != 9:
			ruta.vrid_h()
		else:
			if ruta.kolla_k() != 9: 
				if ruta.kolla_f() == 0:
					ruta.fram()
					steg += 1
					if ruta.check_color() == 2:
						ruta.clean()
			else:
				ruta.vrid_h()
				ruta.vrid_h()
				ruta.fram()
				ruta.fram()
	out = "Klar " + str(steg) + " steg."
	wn.title(out)

def q():
	wn.bye() 

wn.onkey(go, "space")
wn.onkey(q, "q")
wn.listen()
wn.mainloop()