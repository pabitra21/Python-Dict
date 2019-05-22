dict1={1:3,2:3,4:5,6:1}
z=max(dict1.values())
print(z)
for k,v in dict1.items():
    if v==z:
        print(k)

