def fibonacci(n: int):
    if( n == 0 ):
        return 0
    if( n == 1 ):
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

def print_constant():
    print(CONSTANTE_1)


# 1 1 2 3 5 8 11
if __name__ == '__main__':
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8