import turtle
import ruta
wn = turtle.Screen()
ruta.rita_rum()
def q():
	wn.bye() 
wn.onkey(ruta.fram, "Up")
wn.onkey(ruta.vrid_v, "Left")
wn.onkey(ruta.vrid_h, "Right")
wn.onkey(ruta.clean, "space")
wn.onkey(ruta.kolla_r, "r")
wn.onkey(ruta.kolla_k, "k")
wn.onkey(q, "q")
wn.listen()
wn.mainloop()