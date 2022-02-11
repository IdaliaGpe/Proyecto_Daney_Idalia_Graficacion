#Comandos para librerías
#pip install pyopengl
#pip install glfw

#Importar librerias

from sre_constants import JUMP
from OpenGL.GL import *
from glew_wish import *

import glfw
import colision as col

import math

#Variables
velocidad_x = 0.5
velocidad_y = 0.5
JUMP = False
IS_JUMPING = False
IS_FALLING = False

posicion_triangulo = [0.2,0.0,0.0]
posicion_cuadrado = [-0.2, 0.0, 0.0]
posicion_y_cuadrado_anterior = 0.0
window = None

tiempo_anterior = 0.0

#Teclas
def key_callback(window, key, scancode, action, mods):
    #Que la tecla escape cierre ventana al ser presionado
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
         glfw.set_window_should_close(window, 1)

def actualizar():
    global velocidad_x, velocidad_y
    global tiempo_anterior
    global window, JUMP, IS_JUMPING, IS_FALLING 
    global posicion_triangulo
    global posicion_cuadrado
    global posicion_y_cuadrado_anterior 

    tiempo_actual = glfw.get_time()
    #Cuanto tiempo paso entre la ejecucion actual
    #y la inmediata anterior de esta funcion
    tiempo_delta = tiempo_actual - tiempo_anterior

    #Leer los estados de las teclas que queremos
    estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
    estado_tecla_abajo = glfw.get_key(window, glfw.KEY_DOWN)
    estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
    estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)

    cantidad_movimiento = velocidad_x * tiempo_delta
    if estado_tecla_arriba == glfw.PRESS:
        posicion_triangulo[1] = posicion_triangulo[1] + cantidad_movimiento
    if estado_tecla_derecha == glfw.PRESS:
        posicion_triangulo[0] = posicion_triangulo[0] + cantidad_movimiento
    if estado_tecla_abajo == glfw.PRESS:
        posicion_triangulo[1] = posicion_triangulo[1] - cantidad_movimiento
    if estado_tecla_izquierda == glfw.PRESS:
        posicion_triangulo[0] = posicion_triangulo[0] - cantidad_movimiento


    #Movimiento derecha / izquierda
    estado_tecla_d = glfw.get_key(window, glfw.KEY_D)
    estado_tecla_a = glfw.get_key(window, glfw.KEY_A)

    if estado_tecla_d == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] + cantidad_movimiento
    if estado_tecla_a == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] - cantidad_movimiento

    if estado_tecla_d == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] + cantidad_movimiento
    if estado_tecla_a == glfw.PRESS:
        posicion_cuadrado[0] = posicion_cuadrado[0] - cantidad_movimiento

    #Salto
    poder_salto = 1.5
    vel_y = velocidad_y * tiempo_delta * poder_salto
    gravedad = -0.3

    estado_tecla_space = glfw.get_key(window, glfw.KEY_SPACE)
    if JUMP is False and IS_JUMPING is False and estado_tecla_space == glfw.PRESS:
        JUMP = True
        posicion_y_cuadrado_anterior = posicion_cuadrado[1]

    if JUMP is True:
        # Añade a la y la velocidad_y a la velocidad anteiror
        # Añade la velocidad del salto
        posicion_cuadrado[1] += vel_y
        IS_JUMPING = True

    # Ver si ya se paso de burger
    if IS_JUMPING:
        if posicion_cuadrado[1] - posicion_y_cuadrado_anterior >= 0.2:
            # print("Bruhc")
            JUMP = False
            vel_y = gravedad * tiempo_delta
            posicion_cuadrado[1] += vel_y
            IS_FALLING = True

    if IS_FALLING: 
        vel_y = gravedad * tiempo_delta
        posicion_cuadrado[1] += vel_y

    if posicion_cuadrado[1] < 0:
        IS_JUMPING = False
        JUMP = False
        IS_FALLING = False

    tiempo_anterior = tiempo_actual

#Dibujar triangulo
def draw_triangulo():
    global posicion_triangulo
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

def draw_cuadrado():
    global posicion_cuadrado
    glPushMatrix()
    glTranslatef(posicion_cuadrado[0], posicion_cuadrado[1], 0.0)
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.9, 0.21)
    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-0.05,0.05,0.0)
    glVertex3f(0.05,0.05,0.0)
    glVertex3f(0.05,-0.05,0.0)
    glVertex3f(-0.05,-0.05,0.0)
    glEnd()

    glPopMatrix()

#Pintar
def draw():

    draw_cuadrado()
    draw_triangulo()

#Main
def main():
    global window

    width = 700
    height = 700
    #Inicializar GLFW
    if not glfw.init():
        return

    #declarar ventana
    window = glfw.create_window(width, height, "Mi ventana", None, None)

    #Configuraciones de OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Verificamos la creacion de la ventana
    if not window:
        glfw.terminate()
        return

    #Establecer el contexto
    glfw.make_context_current(window)

    #Le dice a GLEW que si usaremos el GPU
    glewExperimental = True

    #Inicializar glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #imprimir version
    version = glGetString(GL_VERSION)
    print(version)

    glfw.set_key_callback(window, key_callback)
    
    #Draw loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        #glViewport(0,0,width,height)
        #Establecer color de borrado
        glClearColor(0.7,0.7,0.7,1)
        #Borrar el contenido del viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        actualizar()
        #Dibujar
        draw()


        #Polling de inputs
        glfw.poll_events()

        #Cambia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()