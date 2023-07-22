a = {1,2,3,4,5}
b = {6,7,8,9,10}
print(a)
print("Type = ",type(a))
s = set({10,20,30})
for i in s:
 print("Iterating through set = ",i)
a.add(6)
print("Adding Element = ",a)
s.update([20,30,40])
print("Updating Set = ",s)
print("\n.....Basic Operations.....\n")
c = a | b
print("Union Operation = ",c)
l = a & b
print("Intersection Operation = ",l)
p = a - b
print("Difference Operation = ",p)
q = a.symmetric_difference(b)
print("Symmetric Difference Operation = ",q)
print("issubset Operation = ",a.issubset(b))
print("issuperset Operation = ",b.issuperset(a))
print("Maximum Item In The Set = ",max(a))
print("Minimum Item In The Set = ",min(a))
print("Sorted Items In The Set = ",sorted(a))
print("Length Of The Set = ",len(a))
