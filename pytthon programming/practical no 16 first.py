import sys
print("Main area starts")
try:
 a = 15 / 0
 print("Division is :-",a)
except ZeroDivisionError:
 print(sys.exc_info()[0],"cannot divided by zero")
finally:
 print("Main area ends")
