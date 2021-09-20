def myFibonacci(n):
    n1, n2 = 0, 1
    count = 0
    s=[]
    if n<=0:
        return False
    elif n ==1:
        return n1
    else:
        fs = []
        while count < n :
            s.append(n1)
            nth = n1+n2
            n1 = n2
            n2 = nth
            count += 1
            sum = 0
            sumHalf =0
            for i in range(len(s)):
                sum += s[i]
            for i in range(int(len(s)/2)):
                sumHalf += s[i]
            fs.append(sum - sumHalf)
        return s, fs

def fiboSequence(n, x):
    s, fs= myFibonacci(n)
    print(s)
    print(fs)
    if x in s or x in fs:
        print("Yes, It is in the sequence")
    else :
        print("No, It is not in sequence")

term = int(input("Enter Terms : "))
x = int(input("Enter value for check : "))
fiboSequence(n=term, x = x)