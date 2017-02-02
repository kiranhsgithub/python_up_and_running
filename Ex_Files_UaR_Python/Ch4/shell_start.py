#
# Example file for working with filesystem shell methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


import os
import shutil
from os import path

def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt");
        
    head ,tail = path.split(src)
    print("path: ", head)
    print("file: ", tail)
      
if __name__ == "__main__":
  main()
