import pyglet
from pyglet.window import key
import numpy as np
import random as rnd
import math

WIDTH = 500
HEIGHT = 500
CUBE_WIDTH = 50
window = pyglet.window.Window(WIDTH,HEIGHT)

def cube_vtx(x1,x2,y1,y2, top=True):
	coords = np.array([[x1,y1],[x2,y1],[x2,y2],[x1,y2]])
	shr = np.array([[0,0],[0.0,-25.0],[0.0,-25.0],[0,0]])
	flip = np.array([[50,-25],[50,0],[50,0],[50,-25]])
	sqsh = np.array([[0,50],[0,25],[50,0],[50,25]])

	east_p = coords + shr
	west_p = coords + flip 
	north_p = coords + sqsh 
	
	if top:
		result = np.concatenate((east_p,west_p,north_p))
	else:
		result = np.concatenate((east_p,west_p))
	
	result = result.flatten()

	return result

def set_color_gray(top=None):
	 e = rnd.randint(0,255)
	 west = (e//2,e//3,e//4,255) * 4 
	 east = (e//3+25,e//2+25,e//2+25,255) * 4 
	 north = (e//3+10,e//2+10,e//4+10,255) * 4

	 if top:
	 	result = (west + east + north)
	 else:
	 	result = (west + east)
	 
	 return result

def make_cube(position,cube_width, top=True):
	center_x = position[0]
	center_y = position[1]
	x1 = center_x - cube_width//2
	x2 = center_x + cube_width//2
	y1 = center_y - cube_width//2
	y2 = center_y + cube_width//2
	cube_verts = cube_vtx(x1,x2,y1,y2,top)
	cube_color = set_color_gray(top)
	
	if top:
		cube_data = (12, pyglet.gl.GL_QUADS, None,('v2f',cube_verts),('c4B',cube_color))
	else:
		cube_data = (8, pyglet.gl.GL_QUADS, None,('v2f',cube_verts),('c4B',cube_color))
	
	return cube_data

batch = pyglet.graphics.Batch()
pos = [250,250]
top = True
@window.event
def on_key_press(symbol, midifiers):

	if symbol == key.W:
		pos[1] += 51
		cube = make_cube([pos[0],pos[1]],CUBE_WIDTH, True)
	if symbol == key.S:
		pos[1] -= 51
		cube = make_cube([pos[0],pos[1]],CUBE_WIDTH, True)
	if symbol == key.A:
		pos[0] -= 51
		pos[1] -= 26
		cube = make_cube([pos[0],pos[1]],CUBE_WIDTH, True)
	if symbol == key.D:
		pos[0] += 51
		pos[1] += 26
		cube = make_cube([pos[0],pos[1]],CUBE_WIDTH, True)
	
	batch.add(cube[0],cube[1],cube[2],cube[3],cube[4])
	

@window.event
def on_draw():
	window.clear()
	batch.draw()

pyglet.app.run()
