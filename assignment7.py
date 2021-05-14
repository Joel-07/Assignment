a=[1,2,3,4,5]
b=["a","b","c","d","e"]
c=[]
d=[5,7,8,9,14]

for i in range(len(a)) :
# print ([list((a[i], b[i])) for i in range(len(a))])
    c.append(list((a[i],b[i],d[i])))

print(c)
#print(dict(c))