import sys

def sum_divisors(x):
    r = 0
    y = 1
    while y <= x:
        if x % y == 0:
            r += 1
        y += 1
    return r

def main(x):
    # Encontrar los divisores de x
    c = sum_divisors(x)
    # Comparación con los números inferiores
    max_divisors = c
    l = x - 1
    while l >= 1:
        if sum_divisors(l) >= max_divisors:
            print("not anti-prime")
            return
        l -= 1

    print("anti-prime")

if __name__ == "__main__":
    x = int(sys.argv[1])
    main(x)

