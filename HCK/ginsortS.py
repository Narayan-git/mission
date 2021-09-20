s = "Sorting123456"
# s= input()
sa =""
ca = ""
nao = ""
nae = ""
for c in s:
    if c.islower():
        sa+=c
    elif c.isupper():
        ca+=c
    elif c.isnumeric():
        if int(c)%2 == 0:
            nae+=c
        else:
            nao+=c
n=""
n+="".join(sorted(nao))
n+="".join(sorted(nae))
na = n
sub = [sa,ca]
res = ""
res+="".join(sorted(sa))
res+="".join(sorted(ca))
res+=na

print(res)