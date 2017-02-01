#
# Example file for working with conditional statements
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main(x=10, y=100):
    
    print("x is", x, ", and y is ", y)
    
    
    if(x < y):
        str = "x is less than y"
    elif (x > y):
        str = "x is greater than y"
    else:
        str = "x is equal to y"
    print("str is ", str)
    
    new_st = "x is less than or equal to y\n" if (x <= y) else "x is greater than y\n"
    print("new_str", new_st)
  
def anotherMain(x=1000,y=10):
    if(x < y):
        st = "x is less than y"
    #uncomment below line
    #print(st)
  
if __name__ == "__main__":
    main()
    main(1000,10)
    main(10,1000)
    main(100,100)
    print("Calling anotherMain Now")
    anotherMain()
