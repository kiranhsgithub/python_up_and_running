#
# Example file for working with loops
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
    x = 0
    while (x < 5):
        print(x)
        x = x + 1
    for x in range(5,10):
        print(x)
    
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for d in days:
        print(d)
        
    print("\nBreak :")
    for x in range(5,10):
        if(x == 7): break
        print(x)
        
    print("\n Continue")
    for x in range(5,10):
        if(x % 2 == 0): continue
        print(x)
        
    print("\n Enumerate")
    for index, value in enumerate(days):
        print(index, value)

if __name__ == "__main__":
    main()
    

