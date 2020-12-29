import turtle
import time
from random import randint

sp_1 = [[1,1,1,1,1,1,1,1,1,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,0],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,0,0,0,0,0,0,0,0,1],
		[1,1,1,1,1,1,1,1,1,1]]


wn = turtle.Screen()
wn.setup(250, 250)
wn.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.ht()
t.penup()
t_ruta = [2, 9]
t.color("green")
t.setheading(180)
r = turtle.Turtle()
r.speed(0)
r.ht()
r.pensize(2)
r.pencolor('black')
r.penup()
r.goto(-100, 100)
ok = 0
pel = 0
dirt = 0

def ruta(a, b, c):
	r.goto(a, b)
	r.pendown()
	r.setheading(0)
	r.fillcolor(c)
	r.begin_fill()
	r.forward(20)
	r.right(90)
	r.forward(20)
	r.right(90)
	r.forward(20)
	r.right(90)
	r.forward(20)
	r.right(90)
	r.end_fill()
	r.penup()

def rita_rum():
	for i in range(12):
		a = randint(1,8)
		b = randint(1,8)
		sp_1[a][b]=2
		# print(a, b)
	for i in range(pel):
		a = randint(1,7)
		b = randint(1,7)
		sp_1[a][b]=1
		# print(a, b)
	for i in range(10):
		wn.tracer(0)
		for j in range(10):
			if sp_1[i][j] == 1:
				ruta(-100+(j*20), 100-(i*20), "red")
			elif sp_1[i][j] == 2:
				ruta(-100+(j*20), 100-(i*20), "gray")
			else:
				ruta(-100+(j*20), 100-(i*20), "orange")
		wn.tracer(1)
	t.goto(90,50)
	t.st()

def fram():
	time.sleep(0.1)
	h = int(t.heading())
	if (h == 0):
		if(sp_1[t_ruta[0]][t_ruta[1]+1] != 1):
			t_ruta[1] += 1
			t.forward(20)
	elif (h == 90):
		if(sp_1[t_ruta[0]-1][t_ruta[1]] != 1):
			t_ruta[0] -= 1
			t.forward(20)
	elif (h == 180):
		if(sp_1[t_ruta[0]][t_ruta[1]-1] != 1):
			t_ruta[1] -= 1
			t.forward(20)
	elif (h == 270):
		if(sp_1[t_ruta[0]+1][t_ruta[1]] != 1):
			t_ruta[0] += 1
			t.forward(20)
	else:
		print("fel")
	# print(t_ruta)

def vrid_v():
	time.sleep(0.1)
	t.left(90)

def vrid_h():
	time.sleep(0.1)
	t.right(90)

def clean():
	time.sleep(0.2)
	x = t.xcor()
	y = t.ycor()
	ruta(x-10, y+10, "orange")
	sp_1[t_ruta[0]][t_ruta[1]] = 0
	t.forward(0)

def check_color():
	c = sp_1[t_ruta[0]][t_ruta[1]]
	return c

def how_many():
	global sp_1
	dirt = 0
	for i in range(len(sp_1)):
		for j in range(len(sp_1[0])):
			if sp_1[i][j] == 2:
				dirt = dirt + 1
	return dirt

def kolla_r():
	return t_ruta[0]
	# print(t_ruta[0])

def kolla_k():
	return t_ruta[1]
	# print(t_ruta[1])

def kolla_f():
	global ok
	h = int(t.heading())
	if (h == 0):
		if(sp_1[t_ruta[0]][t_ruta[1]+1] == 1):
			ok = 1
		else:
			ok = 0
	elif (h == 90):
		if(sp_1[t_ruta[0]-1][t_ruta[1]] == 1):
			ok = 1
		else:
			ok = 0
	elif (h == 180):
		if(sp_1[t_ruta[0]][t_ruta[1]-1] == 1):
			ok = 1
		else:
			ok = 0
	elif (h == 270):
		if(sp_1[t_ruta[0]+1][t_ruta[1]] == 1):
			ok = 1
		else:
			ok = 0
	else:
		print("fel")
	return ok