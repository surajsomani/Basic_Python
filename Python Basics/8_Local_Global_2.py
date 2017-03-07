x = 6

def example4():
    globx = x
    # now we can:
    print(globx)
    globx+=5
    print(globx)
#example4()


x = 6
def example(x):
    print(x)
    x+=5
    print(x)
    return x
#x = example(x)
#print(x)

x = 6
def example5(modify):
 
    print(modify)
    modify+=5
    print(modify)
    return modify 
x = example5(x)
print(x)
