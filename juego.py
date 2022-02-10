#Importar Librerias
from turtle import width
from OpenGL.GL import *
from glew_wish import *
import glfw

#Teclas
#Tecla escape cierre ventana
def key_callback(window, key, scancode, action, mods):
    #Que la tecla escape cierre ventana al ser presionado
    if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
        glfw.set_window_should_close(window, 1)

#Main
def main():
    width = 800
    height = 800

    #Inicializar GLFW
    if not glfw.init():
        return

    #Declarar Ventana
    window = glfw.create_window(width, height, "Mario", None, None)

    #Configuraciones de OPENGL
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

    #Inicializamos glew
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return
    
    #Imprimir Version
    version = glGetString(GL_VERSION)
    print(version)

    #Establecer el key callback
    glfw.set_key_callback(window, key_callback)

    #Draw Loop
    while not glfw.window_should_close(window):
        #Establecer el viewport
        glViewport(0, 0, width, height)
        #Establecer color de borrado
        glClearColor(162/255, 202/255, 223/255, 1)
        #Borrar el contenido de viewport
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        #Dibujar
        #Nos queda pendiente el dibujo

        #Polling de Inputs
        glfw.poll_events()

        #Canbia los buffers
        glfw.swap_buffers(window)

    glfw.destroy_window(window)
    glfw.terminate()

if __name__ == "__main__":
    main()