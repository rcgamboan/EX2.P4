# con X = 3 , Y = 9 , Z = 4
# alpha = ((3+9) mod 5) + 3 = 5
# beta =  ((9+4) mod 5) + 3 = 6
# Con estos valores, siguiendo la definicion de la funcion se tiene

# F(5,6) = F(5,6) (n-6) + F(5,6) (n-12) + F(5,6) (n-18) + F(5,6) (n-24) + F(5,6) (n-30)

# Para calcular F de n, primero se verifica si n esta entre 0 y 30
# si esta entre 0 y 30 se devuelve la posicion de la lista que corresponde a n
# caso contrario se itera n - 29 veces para hallar F de n 
# en cada iteracion, comenzando desde i = 29 para calcular F de n = 30, se usan los valores de F de n-6 , n-12, n-18, n-24 y n-30
# guardando el resultado al final de la lista y corriendo todos los elementos hacia la izquierda un espacio
# cuando i = n, significa que ya se calculo F n y este se encuentra al final de la lista
def f_iter(n):
    
    lista=[i for i in range(0,31)]

    if n in range(0,30):
        return lista[n]
    
    # similar a la version con recursion de cola, en cada iteracion se calcula F de n = i+1
    # usando los valores que ya se encuentran en la lista en las posiciones n-6 , n-12, n-18, n-24 y n-30
    # hasta alcanzar al n solicitado
    i = 29
    while i != n:
        lista[-1] = lista[24] + lista [18] + lista[12] + lista[6] + lista[0]
        for j in range(1,len(lista)):
            lista[j-1] = lista[j]
        i += 1
    
    return lista[-1]

#print(f_iter(100000))
    