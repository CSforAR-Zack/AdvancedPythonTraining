# basics_02.py

def main():
    # Arithmetic: () ** * / // % + -
    # Concatenation: + * <-- duplicate n times
    # Relational: == != < > <= >=
    # Logical: and, or, not
    # Unirary Operators: + - (-1)

    print('The square of 4 is', numSquarer(4), sep=': ', end=' - ')
    print('The square of 4 is', numSquarer(4), sep=': ')

    print('First line')
    print('Second line')

def numSquarer(num):
    '''This takes a number and 
    returns the square of it.
    '''
    return num * num

if __name__ == '__main__':
    main()

