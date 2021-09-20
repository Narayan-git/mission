'''
input  : s = "AABCAAADA", k= 3
output :
        AB
        CA
        AD
'''

def merge_the_tools(s, k):
    usa = []
    res = []
    for i in range(0,len(s),k):
        usa.append(s[i:i+k])
        t=""
        for c in s[i:i+k]:
            if c not in t:
                t+=c
        res.append(t)
    return res

s= input("Enter a String : ")
k = int(input("Enter Value of K : "))

print (merge_the_tools(s, k))
