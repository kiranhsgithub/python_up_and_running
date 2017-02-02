#
# Example file for working with filesystem shell methods
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)


import os
import shutil
from os import path
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("textfile.txt"):
        src = path.realpath("textfile.txt");
        
    head ,tail = path.split(src)
    print("path: ", head)
    print("file: ", tail)
    
    dst = src + ".bak"
    shutil.copy(src,dst)
    
    dst2 = src + ".bak2"
    shutil.copy(src,dst2)
    shutil.copystat(src,dst2)
    
    #os.rename(src + ".bak2","newfile.txt")
    
    root_dir, tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir)
    
    with ZipFile("testing.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")
      
if __name__ == "__main__":
  main()
