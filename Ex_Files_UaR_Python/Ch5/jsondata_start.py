# 
# Example file for parsing and processing JSON
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

import urllib.request
import json

def printResults(data):
    theJSON = json.loads(data)
    
    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])
    
    count = theJSON["metadata"]["count"];
    print(str(count) + "events recorded")
    
    for i in theJSON["features"]:
        print(i["properties"]["place"])
        
    for i in theJSON["features"]:
        if i["properties"]["mag"] >= 4.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
            
    print("Events that were felt")
    for i in theJSON["features"]:
        feltReports = i["properties"]["felt"]
        if feltReports != None:
            if feltReports > 0:
                print("%2.1f" % i["properties"]["mag"], i["properties"]["place"], " reported " + str(feltReports) + " times")
    
def main():
    # define a variable to hold the source URL
    # In this case we'll use the free data feed from the USGS
    # This feed lists all earthquakes for the last day larger than Mag 2.5
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    
    webUrl = urllib.request.urlopen(urlData)
    print(webUrl.getcode())
    if(webUrl.getcode() == 200):
        data = webUrl.read()
        printResults(data)
    else:
        print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
  

if __name__ == "__main__":
  main()
