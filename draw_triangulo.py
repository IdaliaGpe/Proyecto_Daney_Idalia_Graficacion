from sre_constants import JUMP
from OpenGL.GL import *
from glew_wish import *

import colision as col
import glfw

def draw_triangulo(posicion_triangulo, posicion_cuadrado):
    
    glPushMatrix()
    glTranslatef(posicion_triangulo[0], posicion_triangulo[1],0.0)
    glBegin(GL_TRIANGLES)

    #Establecer color    
    if col.colision(posicion_triangulo, posicion_cuadrado):
        glColor3f(0,0,1)
    else:
        glColor3f(1,0,0)

    #Manda vertices a dibujar
    glVertex3f(-0.05,-0.05,0)
    glVertex3f(0.0,0.05,0)
    glVertex3f(0.05,-0.05,0)

    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0.0,0.0,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)

    glEnd()

    glPopMatrix()