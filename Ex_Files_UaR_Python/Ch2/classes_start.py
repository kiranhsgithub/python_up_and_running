#
# Example file for working with classes
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

class myClass():
    def method1(self):
        print("myClass method1")
    
    def method2(self, something):
        print("my class method2: " + something)  

class anotherClass(myClass):
    def method2(self):
        print("anotherClass method2")
        
def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")
    c2 = anotherClass()
    c2.method1()
    c2.method2()
    c2.method2("another String")

  
if __name__ == "__main__":
  main()
