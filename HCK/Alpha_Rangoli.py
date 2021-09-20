'''
#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

'''
def print_rangoli(size):
    # your code goes here
    l = list(map(chr, range(97, 123)))
    n = size
    x = len("-".join(l[n-1::-1] + l[1:n]))
    for i in range(1, n):
        print("-".join(l[n-1:n-i:-1]+l[n-i:n]).center(x, "-"))
    
    for i in range(n, 0, -1):
        print("-".join(l[n-1:n-i:-1]+l[n-i:n]).center(x, "-"))
