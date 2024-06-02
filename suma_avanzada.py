
def suma_avanzada(data):
    resultado = 0
    num_datos = len(data)
    for x in range(1, num_datos):
        resultado += data[x]
    return(resultado)