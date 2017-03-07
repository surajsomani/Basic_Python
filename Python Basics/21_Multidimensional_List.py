#Lets take the below multi dimensional list and see how it looks
x = [[2,6],[6,2],[8,2],[5,12]]
print(x[2])
#we will see that x[2] is a list inside list x
#to dig down to element we do
print(x[2][1])
#here we see the list at index 2 in x and the value at index of 1 in x[2]
y = [[5,2],
     [6,2],
     [3,1],
     [12,6]
    ]
#python will automaticlly understand that the above is a list of list
print(y)
