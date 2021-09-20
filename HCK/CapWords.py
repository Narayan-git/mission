
s= "hello   world  lol"
s="1 w 2 r 3g"
r=""
for i in range(len(s)):
    if(i == 0):
        r=s[i].upper()
    elif s[i].islower() and s[i-1]==" ":
        r+=s[i].upper()
    else:
        r+=s[i]

print(r)