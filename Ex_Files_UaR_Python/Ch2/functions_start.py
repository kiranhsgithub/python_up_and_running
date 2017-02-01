#
# Example file for working with functions
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def func1():
    print("I am a function")
    return "return value"
    
func1()
print(func1())
print(func1)

def func2(arg1, arg2):
    print(arg1,", ", arg2)

#uncomment below line and fails    
#func2(10)

func2(10,20)
func2("Hello","World!")

#more number of arguments are not taken
#func2(10,"Hello",20)


def cube(x):
    return x * x * x

print(cube(3))
    
def power(num, x=1):
    result = 1;
    for i in range(x):
        result = result * num
    return result

print(power(2))
print(power(2,3))
print(power(x=2, num=5))

def multi_add(*args):
    result=0;
    for x in args:
        result = result + x
    return result

print(multi_add(4,5,10,4))
print(multi_add(4,5,10,4,10))
