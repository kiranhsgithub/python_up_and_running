#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

from datetime import date
from datetime import time 
from datetime import datetime

def main():
    today = date.today()
    print("Today's date is ", today)
    
    print("Date Components: ", today.day, today.month, today.year)
    
    print("Today's Weekday #: ", today.weekday())
    
    today = datetime.now()
    print("The current date and time is :", today)
    
    time = datetime.time(datetime.now())
    print("The current time is : ", time)
    
    wd = date.weekday(today)
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print("Today is day number %d" % wd)
    print("Which is a ", days[wd])
  
  
if __name__ == "__main__":
  main();
  