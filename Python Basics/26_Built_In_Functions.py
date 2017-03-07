#absolute values
exNum1 = -5
exNum2 = 5
print(abs(exNum1))
if abs(exNum1) == exNum2:
    print('True!')

#using help function
import time
# will work in a typical installation of Python, but not in the embedded editor
help(time)

#Max and Min
exList = [5,2,1,6,7]

largest = max(exList) #get maximum value from the list
print(largest)

smallest = min(exList) #get minimum value from the list
print(smallest)

#Rounding
x = 5.622
x = round(x)
print(x)
y = 5.256
y = round(y)
print(y)
z = 5.5
z = round(z)
print(z)

#string to integer
intMe = '55'
intMe = int(intMe)
print(intMe)

#converting Integer to String
stringMe = 55
stringMe = str(stringMe)
print(stringMe)

#integer to float
floatMe = 55
floatMe = float(floatMe)
print(floatMe)

