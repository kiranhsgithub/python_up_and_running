# 
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

f = 0;
print(f)

f = "original"
print(f)

#print("String type " + 123)

print("String type " + str(123))

def someFunction():
    f = "someFunction"
    print(f)

def someOtherFunction():
    global f
    f = "someOtherFunction"
    print(f)
    
someFunction()
someOtherFunction()
print(f)

del f
#uncomment below to see error
#print(f)
     