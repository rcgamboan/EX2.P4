
# con X = 3 , Y = 9 , Z = 4
# alpha = ((3+9) mod 5) + 3 = 5
# beta =  ((9+4) mod 5) + 3 = 6
# Con estos valores, siguiendo la definicion de la funcion se tiene

# F(5,6) = F(5,6) (n-6) + F(5,6) (n-12) + F(5,6) (n-18) + F(5,6) (n-24) + F(5,6) (n-30)

# implementacion recursiva de la funcion F(5,6)
# para calcular F(5,6) de n, se llama recursivamente a F con n-6 , n-12, n-18, n-24 y n-30
def f_recursiva(n):

    if 0<=n<30:
        return n
    else:
        return f_recursiva(n-6) + f_recursiva(n-12) + f_recursiva(n-18) + f_recursiva(n-24) + f_recursiva(n-30)

#print(f_recursiva(250))