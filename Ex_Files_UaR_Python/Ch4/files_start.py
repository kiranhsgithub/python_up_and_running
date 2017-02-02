#
# Read and write files using the built-in Python file methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():  
    f = open("textfile.txt", "w+")
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
        
    f.close()
    
    f = open("textfile.txt", "a+")
    for i in range(10):
        f.write("This is new line %d \r\n" % (i + 1))
        
        
    f = open("textfile.txt", "r")
    if(f.mode == 'r'):
        fl = f.readlines()
        
        print("Line by Line")
        for x in fl:
            print(x)
    
    f = open("textfile.txt", "r")
    if(f.mode == 'r'):
        contents = f.read()
        print("All contents")
        print(contents)
    
    
if __name__ == "__main__":
  main()
