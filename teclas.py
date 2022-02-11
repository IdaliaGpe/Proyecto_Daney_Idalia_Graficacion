from sre_constants import JUMP
from OpenGL.GL import *
from glew_wish import *

import glfw

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