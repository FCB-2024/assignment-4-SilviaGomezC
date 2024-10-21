## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(x):
  ## YOU CODE SHOULD START HERE AST THE SAME
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

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__":
    # Definición de la variable x con input del usuario
    x = int(input("Enter a positive integer number: "))
    # Llamada a main(x)
main(x)

	## IDENTATION AS THIS COMMENT
	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
