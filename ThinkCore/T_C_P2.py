def DecrNum(num):
    strnum=str(num)
    i=0
    flag=0
    while i <(len(strnum)-1):
        diff=ord(strnum[i])-ord(strnum[i+1])
        if (diff <2):
            flag=1
            break
        i+=1

    if(flag==0):
        return True
    else:
        return False


def IncrNum(num):
    strnum=str(num)
    i=0
    flag=0
    while i <(len(strnum)-1):
        diff=ord(strnum[i+1])-ord(strnum[i])
        if (diff <2):
            flag=1
            break
        i+=1

    if(flag==0):
        return True
    else:
        return False

ODDSUM=0
ODDminusEVENsum=0
SQROOTPROD=0
for num in range(100,100001):
    if(IncrNum(num)==True):
        strnum=str(num)
        ln=len(strnum)
        j=ln-1
        digitsum=0
        while(j>=0):
            digitsum+=int(strnum[j])
            j-=2
        print("ODDSUM of ",num ," is ",digitsum)
        ODDSUM+=digitsum

    elif(DecrNum(num)==True):
        strnum=str(num)
        ln=len(strnum)
        j=ln-1
        evendigitsum=0
        odddigitsum=0
        while(j>=0):
            if(j%2==0):
                evendigitsum+=int(strnum[j])
            else :
                odddigitsum+=int(strnum[j])
            
            j-=1
        ODDsum_minus_EVENsum=evendigitsum-odddigitsum
        #odd index means even place and vice varsa
        print("ODDminusEVENsum of ",num ," is ",ODDsum_minus_EVENsum)
        ODDminusEVENsum+=ODDsum_minus_EVENsum
    else:
        strnum=str(num)
        ln=len(strnum)
        j=ln-1
        prod=1
        import math
        while(j>=0):
           sqroot=math.sqrt(int(strnum[j]))
           prod*=sqroot
           j-=1 
        print("SQROOTPROD of ",num ," is ",prod)
        SQROOTPROD+=prod
print("Total ODDSUM is",ODDSUM)
print("Total ODDminusEVENsum is",ODDminusEVENsum)
print("Total SQROOTPROD is",SQROOTPROD)

