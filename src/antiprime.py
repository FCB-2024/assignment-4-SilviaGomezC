## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x):
    # Encontrar los divisores de x
    r = 0
    y = 1
    while y <= x:
        if x % y == 0:
            r += 1
        y += 1

    # Comparación con los números inferiores
    max_divisors = r
    i = 1
    while i < x:
        r_i = 0
        y = 1
        while y <= i:
            if i % y == 0:
                r_i += 1
            y += 1
        if r_i >= max_divisors:
            print("not anti-prime")
            return    
        i += 1

    # Imprimir resultado
    print("anti-prime")

if __name__ == "__main__":
    # Definición de la variable x con input del usuario
    x = int(input("Enter a positive integer number: "))
    # Llamada a main(x)
main(x)



