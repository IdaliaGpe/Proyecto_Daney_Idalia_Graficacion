def colision(posicion_triangulo, posicion_cuadrado):
    colisionando = False
    #Extrema derecha del triangulo >= Extrema izquierda cuadrado
    #Extrema izquierda del triangulo <= Extrema derecha cuadrado
    #Extrema superior del triangulo >= Extrema inferior cuadrado
    #Extrema inferior del triangulo <= Extrema superior cuadrado
    if (posicion_triangulo[0] + 0.05 > posicion_cuadrado[0] - 0.05 
    and posicion_triangulo[0] - 0.05 <= posicion_cuadrado[0] + 0.05 
    and posicion_triangulo[1] + 0.05 > posicion_cuadrado[1] - 0.05 
    and posicion_triangulo[1] - 0.05 <= posicion_cuadrado[1] + 0.05):
        colisionando = True
    return colisionando