d1 = {'a':100,'b':200,'c':300}
d2 = {'a':300,'b':200,'d':400}
d1.update(d2)
for key,values in d1.items():
print(key,values)
