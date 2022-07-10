# con X = 3 , Y = 9 , Z = 4
# alpha = ((3+9) mod 5) + 3 = 5
# beta =  ((9+4) mod 5) + 3 = 6
# Con estos valores, siguiendo la definicion de la funcion se tiene

# F(5,6) = F(5,6) (n-6) + F(5,6) (n-12) + F(5,6) (n-18) + F(5,6) (n-24) + F(5,6) (n-30)

# implementacion con recursion de cola de la funcion F(5,6)
# inicialmente se tiene una lista con los valores de la funcion para 0<=n<30
# si se llama a F con n >= 30 se calcula F n sumando los valores de las posiciones n-6 , n-12, n-18, n-24 y n-30 de la lista
# mientras que n sea menor al indice, se repite este proceso y se corren hacia la izquierda los elementos de la lista
# cuando n = indice + 1, significa que el valor de F de n es la suma de las posiciones n-6 , n-12, n-18, n-24 y n-30 de la lista


def f_cola(n,indice=29,lista=[i for i in range(0,31)]):

    
    # Si n = indice + 1 se suman las posiciones n-6 , n-12, n-18, n-24 y n-30 de la lista que representan los valores
    # de aplicar F a  n-6 , n-12, n-18, n-24 y n-30 respectivamente
    if n == indice+1:
        
        return lista[24] + lista [18] + lista[12] + lista[6] + lista[0]
    
    # Caso contrario, se sustituye el ultimo elemento de la lista con su valor al aplicar F y se corren todos los elementos
    # una posicion a la izquierda
    else:
        
        lista[-1] = lista[24] + lista [18] + lista[12] + lista[6] + lista[0]

        for i in range(1,len(lista)):
            lista[i-1] = lista[i]
        
        return f_cola(n, indice+1, lista)

#print(f_cola(500))
    
