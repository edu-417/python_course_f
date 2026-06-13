primes = [2, 3, 5, 7, 11, 13, 17, 23, 29]

def isPrime(number: int):
    return number in primes

def print_constant():
    print(CONSTANTE_1)


# print(__name__)
if (__name__ == '__main__'):
    assert isPrime(4) == False
    assert isPrime(7) == True