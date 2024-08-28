a= input("enter string ")
string1= ""
r=a.split()
#a1=r[0]
#b1=a1[::-1]
#print(b1)
s= len(r)
for i in range(0,s):
    a1=r[i]
    b1= a1[::-1]
    string1+=b1+" "
print (string1)
