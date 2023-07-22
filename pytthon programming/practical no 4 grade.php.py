a=float(input("MAD marks="))
b=float(input("MGT marks="))
c=float(input("ETI marks="))
d=float(input("PWP marks="))
e=float(input("WBP marks="))
f=a+b+c+d+e
print(f)
avarage=f/5
print("avarage=",avarage)
if(avarage<35):
    print("fail")
elif(avarage>35 and avarage<60):
    print("C")
elif(avarage>60 and avarage<75):
    print("B")
elif(avarage>75 and avarage<100):
    print("A")
elif(avarage<=100):
    print("congratulations!!!")


