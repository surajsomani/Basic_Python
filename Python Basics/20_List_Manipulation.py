# first we need an example list:
x = [1,6,3,2,6,1,2,6,7]
# lets add something.
# we can do .append, which will add something to the end of the list, like:
x.append(55)
print(x)
x.insert(2,33)
#we want to insert, at the index of 2, the number 33
print(x)
#we want to remove the first instance of number "6" 
x.remove(6)
print(x)
#index starts from 0
print(x[5]) #returns the value at index 5
print(x.index(1)) #returns the index of the 1st instance of number "1"
print(x.count(1)) #Count number of instances of 1
x.sort() #Sorting the list x in ascending order
print(x)
#Lets see if list is of String
y = ['Jan','Dan','Bob','Alice','Jon','Jack']
y.sort()
print(y)
y.reverse() #sort descending
print(y)
