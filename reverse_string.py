s =['s','t','r','i','n','g']

print (s)

temp=[]

for i in reversed(range(len(s))):
    temp.append(s[i])


s=temp

print (s)