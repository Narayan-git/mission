def print_formatted(number):
    # your code goes here
    l = len("{0:b}".format(number))
    for i in range(1, number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i, w=l))
        '''
            {w} is used for ju8stifying the other numbers
            {0:{w}d} = for decimal
            {0:{w}o} = for octal
            {0:{w}x} = for hexadecimal
            {0:{w}b} = for binary
        '''
print_formatted(17)