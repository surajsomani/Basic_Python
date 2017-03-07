#Function Definition
def example():
    print('this code will run')
    z = 3 + 9
    print(z)
#Function call
example()
#Function Parameters
def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is', num1)
    print(answer)
simple_addition(5,3)
simple_addition(num2=3,num1=5)
#simple_addition(3,5,6)
#simple_addition(3)
#default parameters and its use
def simple(num1, num2=5):
    print('num1 is', num1)
    pass
simple(7)
def basic_window(width,height,font='TNR'):
    # let us just print out everything
    print(width,height,font)
basic_window(350,500)
basic_window(350,500,font='courier')
