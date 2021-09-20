# check accepctance
def accepectanceCheck(s):
    import re
    r = "[a-z0-9]$"
    if re.search(r,s):
        return True
    else :
        return False

# find longest sequence
def longestSequence(s):
    value=[]
    prev=0
    sl=[]
    for i in range(1,len(s)-1):
        value=ord(s[i])-ord(s[i+1])
        if value<0:
            value*=-1
        if(value==1):
            sl.append(s[i])
            prev=1
            continue
        if(prev==1):
            sl.append(s[i])
            value.append(sl)
            prev=0
            sl=[]
    fq=[]
    for i in range(len(value)):
        fq.append(len(value[i]))
    posi=max(fq)
    subs=[]
    for i in range(len(value)):
        if (posi==len(value[i])):
            ans=''
            for j in range(len(value[i])):
                ans+=value[i][j]
            subs.append(ans)
    return subs

# main function
def Main() :
    s = input("Enter a String : ")
    if accepectanceCheck(s):
        sub = longestSequence(s)
    print(sub)

Main()