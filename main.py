
from dividir import dividir
from multiplicacion import multiplicar
from sumar import sumar
from resta import restar
from suma_avanzada import suma_avanzada

def menu():
    print('')
    print('')
    print('    Calculadora Básica')
    print('')
    print('     Menú de Operaciones')
    print("'S' ------------------ para Sumar")
    print("'R' ------------------ para Restar")
    print("'M' ------------------ para Multiplicar")
    print("'D' ------------------ para Dividir")
    print("'A' ------------------ para Suma Multiple")
    print("'Q' ------------------ para Salir")
    print('')
    seleccion = input('Selecciona del menú la operación deseada: ')
    seleccion = seleccion.lower()
    return(seleccion)

def validacion_operacion(seleccion):
    validacion = False
    operaciones = ['s','r','m','d','a','q']
    while validacion == False:
        for opcion in operaciones:
            if opcion == seleccion:
                validacion = True      
                break
        if validacion == False:
            print('')
            print('Opcion invalida....Selecciona una opción del menú')
            seleccion = menu()
    return seleccion

def validacion_datos(data):
    val_datos = True
    try:
        test = data[1]/data[2]
    except:
        print('')
        print('Datos Erroneos')
        print('Introdusca denuevo los datos')
        print('')
        val_datos = False

    return(val_datos)

def respuesta(data, resultado, operacion):
    print('*****************************************************')
    print('')
    print( ' El resultado de la ' + data[0] + ' es: ')
    print('')
    y = len(data)
    print(' (', end ='')
    for x in range(1,y-1):

        print(str(data[x])+operacion, end ='')
    print(str(data[y-1])+ ') = '+ str(resultado))
    print('')
    print('*****************************************************')
   

def datos(seleccion):

    data = []
    operaciones = {'s':['SUMA','Primer Sumando','Segundo Sumando'],
                   'r':['RESTA','Minuendo','Sustraendo'],
                   'm':['MULTIPLICACION','Multiplicando','Multiplicador'],
                   'd':['DIVISION','Dividendo','Divisor'],
                   'a':['SUMA MULTIPLE','Primer Sumando','Siguiente Sumando']}
    
    info = operaciones[seleccion]
    data.append(info[0])
    print('')
    if seleccion !='a':
        print('Operación '+ data[0])
        a = float(input('Introdusca el '+ info[1]+ ' :'))
        data.append(a)
        b = float(input('Introdusca el '+ info[2]+ ' :'))
        data.append(b)
        
    else:
        print('   Operación '+ data[0])
        print('--------------------------------------------------------------')
        print('Para terminar de introdocir los Sumandos solo introduce " = "')
        print('')
        a = input('Introdusca el '+ info[1] + '...... ')
     
        run = True
        while run:
            try:
                a = float(a)
                data.append(a)
                a = (input('Introdusca el '+ info[2] + '... '))
            except:
                if a == '=':
                    run = False
                else:
                    print('')
                    print('Datos Erroneos')
                    a = (input('Introdusca denuevo el dato: '))

    return(data)






seleccion = menu()
seleccion = validacion_operacion(seleccion)

while seleccion !=  'q':
    
    data = datos(seleccion)
    val_data = validacion_datos(data)
    while val_data == False:
        data = datos(seleccion)
        val_data = validacion_datos(data)

    if seleccion == 'd':
        operacion = ') / ('
        resultado = dividir(data)
    if seleccion == 'm':
        operacion = ') * ('
        resultado = multiplicar(data)
    if seleccion == 's':
        operacion = ') + ('
        resultado = sumar(data)
    if seleccion == 'r':
        operacion = ') - ('
        resultado = restar(data)
    if seleccion == 'a':
        operacion = ') + ('
        resultado = suma_avanzada(data)


    respuesta(data, resultado, operacion)

    print('          Opimir <ENTER> para continuar')
    input()
    seleccion = menu()
    seleccion = validacion_operacion(seleccion)
    
    





       
    





