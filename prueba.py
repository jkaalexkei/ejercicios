
#decoradores

def fizzbuzz(numero):
    
    if (numero % 3 == 0) and (numero % 5 == 0):
        return 'fizzbuzz'
    
    elif numero % 5==0:
        return 'fizz'
    elif numero % 3 == 0:
        return 'buzz'
    else:
        return numero
        

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in range(1,21):
    print(fizzbuzz(i))

