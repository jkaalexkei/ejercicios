
#decoradores

# def fizzbuzz(numero):
    
#     if (numero % 3 == 0) and (numero % 5 == 0):
#         return 'fizzbuzz'
    
#     elif numero % 5==0:
#         return 'fizz'
#     elif numero % 3 == 0:
#         return 'buzz'
#     else:
#         return numero
        

# lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# for i in lista:
#     print(fizzbuzz(i))


def palindromo(texto):
    
    lista = []
    
    for elementos in texto:
        
        lista.append(elementos)
        
    textocontrario = lista[::-1]
    
    comparacion = 'palindromo' if lista == textocontrario else 'no es palindromo'
    
    return comparacion

print(palindromo('ana'))


#CLOSURE

def closure(texto):
    
    info = texto
    
    def interna():
        
        print('funcion interna y el mesaje externo es %s' %(info))
    
    return interna


mensaje = closure('hola mundo')

mensaje()


#decoradores

def FuncionA(FuncionB):
        
    print('mensaje de la funcion A')
        
    def FuncionC():
            
        print('mensaje inicial de la funcion C')
        FuncionB()
        print('mensaje final de la funcion C')
            
    return FuncionC()

@FuncionA
def saludar():
    print('HOLA MUNDO')
    


def measure_time(function):
    def wrapper(*args, **kwargs):
        import time

        start = time.time()
        result = function(*args, **kwargs)
        total = time.time() - start
        print(total, 'seconds' )
        return result

    return wrapper


@measure_time
def suma(a, b):
    import time
    time.sleep(1)
    return a + b

print(suma(10, 20))