nterms = int(input("How Many Terms = "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
 print("Please enter a positive number !!!")
elif nterms == 1:
 print("Fibonnaci Sequence Upto ",nterms,"=")
 print(n1)
else:
 print("Fibonnaci Sequence :- ")
while count < nterms:
 print(n1)
 nth = n1 + n2
 #update values
 n1 = n2
 n2 = nth
 count += 1