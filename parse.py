from xml.etree import ElementTree
import webbrowser
import datetime
today = datetime.datetime.today()
import csv
import pickle
from collections import defaultdict
from collections import OrderedDict
from collections import Counter
from operator import itemgetter


brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"  
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))


Element =[]
Allitems =[]

with open('productor-export.csv', 'r', encoding="utf-8") as f:
    cf = csv.reader(f, delimiter=',')
    
    i= 0
    for row in cf:                          # column index
        for x in row:
            print (i, x)
            i+=1

        break

    for row in cf:  

        Element =[]
        Colours = []
        Last = []
        Element.append(row[17])              # 0 DesignID
        
        Element.append(row[1])               # 1 Title
        Element.append(row[11])              # 2 Marketplace
        
        Element.append(row[6])              # 3 Men
        Element.append(row[7])              # 4 Women
        Element.append(row[8])              # 5 Kids
        Element.append(row[12])              # 6 Product Type
        Element.append(row[32])              # 7 Sold Colours
        
        for x in range(43, 72):
            row[x] = row[x].replace("_", " " ) 
            row[x] = row[x].title()
            

        Colours.extend(row[43:72])            # 8 Colours 
        Colours[:] = [item for item in Colours if item != '']
        Element.append(Colours)
        
        
        date = datetime.datetime.strptime(str(row[40]), '%B %d, %Y %I:%M %p')
        Last.append(date)
        
        if len(row[22]) > 0:
            date = datetime.datetime.strptime(str(row[22]), '%m/%d/%Y') 
            Last.append(date)

        Element.append(Last)                # 9 Last Update
        Element.append(row[5])              # 10 Description
        Element.append(row[34])             # 11 URL
       
        price = float(row[2])                # 12 Price
        if price > 100:
            price = price/100
        Element.append(price)             

        

        if row[18] == "TIMED_OUT":
            if (str(price)[-1]) == "8":
                row[18] = row[18]+"_OK"
        Element.append(row[18])             # 13 Status
        
        
        sold = 0
        if len(row[23]) >0:
            sold = int(row[23])
        Element.append(sold)             # 14 Sold Alltime
        
        Allitems.append(Element)


DesignID = defaultdict(list)

for x in Allitems:                              #Expiring check
    DesignID[x[0]].extend(x[9])
    
for x in DesignID:
    DesignID[x] = max(DesignID[x])
    DesignID[x] = -(today - datetime.timedelta(days=365) - DesignID[x])

d = OrderedDict(sorted(DesignID.items(), key=itemgetter(1), reverse=True))

Description = [
    "Frequent Traveller Souvenir, Vacation, First Class, Jet Set, Aviation, Pilot, present, Christmas, xmas, birthday, anniversary, mom, dad, son, daughter, grandpa, grandad, granny, grandma, mother's day, father's day, airplane, aeroplane", 
    "present, Christmas, xmas, birthday, anniversary, mom, dad, son, daughter, grandpa, grandad, granny, grandma, mother's day, father's day, travels, vacation, travelling, holidays"
]

color_counts = {
    "Standard T-Shirt": 29,
    "Premium T-Shirt": 21,
    "V-neck T-Shirt": 10,
    "Tank Top": 10,
    "Long Sleeve T-Shirt": 5,
    "Raglan": 7,
    "Sweatshirt": 5,
    "Pullover Hoodie": 15,
    "Zip Hoodie": 8,
    "PopSockets Grip": 1,
    "iPhone Cases": 1,
    "Samsung Galaxy Cases": 1,
    "Tote Bag": 1,
    "Throw Pillows": 1,
    "Tumbler": 3,
}

deprecated_products = ["Samsung Galaxy Cases",]
deprecated = 0

minPricelist = {"US": {"Standard T-Shirt": 14.99, "Premium T-Shirt": 16.99, "V-neck T-Shirt": 16.99, "Tank Top": 16.99, "Long Sleeve T-Shirt": 19.99, "Raglan": 20.99, "Sweatshirt": 26.99, "Pullover Hoodie": 26.99, "Zip Hoodie": 28.99, "PopSockets Grip": 11.99, "iPhone Cases": 15.99, "Tote Bag": 16.99, "Throw Pillows": 18.99, "Tumbler": 20.99},
                "GB": {"Standard T-Shirt": 13.99,                           "V-neck T-Shirt": 14.99, "Tank Top": 14.99, "Long Sleeve T-Shirt": 18.99, "Raglan": 16.99, "Sweatshirt": 25.99, "Pullover Hoodie": 27.99, "Zip Hoodie": 24.99, "PopSockets Grip":  9.99, "iPhone Cases": 13.99},
                "DE": {"Standard T-Shirt": 15.99,                           "V-neck T-Shirt": 15.99, "Tank Top": 15.99, "Long Sleeve T-Shirt": 19.99, "Raglan": 17.99, "Sweatshirt": 27.99, "Pullover Hoodie": 30.99, "Zip Hoodie": 27.99, "PopSockets Grip": 10.99, "iPhone Cases": 14.99},
                "FR": {"Standard T-Shirt": 15.99,                           "V-neck T-Shirt": 16.99, "Tank Top": 15.99, "Long Sleeve T-Shirt": 17.99, "Raglan": 18.99, "Sweatshirt": 24.99, "Pullover Hoodie": 27.99, "Zip Hoodie": 26.99, "PopSockets Grip": 12.99, "iPhone Cases": 15.99},
                "IT": {"Standard T-Shirt": 15.99,                           "V-neck T-Shirt": 16.99, "Tank Top": 15.99, "Long Sleeve T-Shirt": 17.99, "Raglan": 18.99, "Sweatshirt": 24.99, "Pullover Hoodie": 27.99, "Zip Hoodie": 27.99, "PopSockets Grip": 12.99, "iPhone Cases": 15.99},
                "ES": {"Standard T-Shirt": 14.99,                           "V-neck T-Shirt": 15.99, "Tank Top": 15.99, "Long Sleeve T-Shirt": 17.99, "Raglan": 18.99, "Sweatshirt": 24.99, "Pullover Hoodie": 26.99, "Zip Hoodie": 26.99, "PopSockets Grip": 11.99, "iPhone Cases": 15.99},
                "JP": {"Standard T-Shirt": 17.99,                                                                       "Long Sleeve T-Shirt": 23.99,                  "Sweatshirt": 31.99, "Pullover Hoodie": 35.99, "Zip Hoodie": 38.99,                           "iPhone Cases": 17.99},
                }
 
maxPricelist = {"US": {"Standard T-Shirt": 21.99, "Premium T-Shirt": 23.99, "V-neck T-Shirt": 23.99, "Tank Top": 23.99, "Long Sleeve T-Shirt": 26.99, "Raglan": 26.99, "Sweatshirt": 33.99, "Pullover Hoodie": 33.99, "Zip Hoodie": 35.99, "PopSockets Grip": 19.99, "iPhone Cases": 20.99, "Tote Bag": 22.99, "Throw Pillows": 23.58, "Tumbler": 22.99},
                "GB": {"Standard T-Shirt": 19.58,                           "V-neck T-Shirt": 22.99, "Tank Top": 21.28, "Long Sleeve T-Shirt": 26.99, "Raglan": 22.08, "Sweatshirt": 33.99, "Pullover Hoodie": 35.99, "Zip Hoodie": 32.99, "PopSockets Grip": 19.99, "iPhone Cases": 17.99},
                "DE": {"Standard T-Shirt": 23.99,                           "V-neck T-Shirt": 23.99, "Tank Top": 24.99, "Long Sleeve T-Shirt": 27.99, "Raglan": 25.99, "Sweatshirt": 36.99, "Pullover Hoodie": 38.99, "Zip Hoodie": 36.99, "PopSockets Grip": 19.99, "iPhone Cases": 19.99},
                "FR": {"Standard T-Shirt": 22.99,                           "V-neck T-Shirt": 23.99, "Tank Top": 22.99, "Long Sleeve T-Shirt": 23.78, "Raglan": 24.68, "Sweatshirt": 32.99, "Pullover Hoodie": 33.08, "Zip Hoodie": 34.99, "PopSockets Grip": 19.99, "iPhone Cases": 19.99},
                "IT": {"Standard T-Shirt": 22.99,                           "V-neck T-Shirt": 23.99, "Tank Top": 22.99, "Long Sleeve T-Shirt": 23.88, "Raglan": 24.78, "Sweatshirt": 32.99, "Pullover Hoodie": 35.99, "Zip Hoodie": 35.99, "PopSockets Grip": 19.99, "iPhone Cases": 19.99},
                "ES": {"Standard T-Shirt": 22.99,                           "V-neck T-Shirt": 23.99, "Tank Top": 23.99, "Long Sleeve T-Shirt": 25.99, "Raglan": 26.99, "Sweatshirt": 32.99, "Pullover Hoodie": 34.99, "Zip Hoodie": 34.99, "PopSockets Grip": 19.99, "iPhone Cases": 19.99},
                "JP": {"Standard T-Shirt": 24.26,                                                                       "Long Sleeve T-Shirt": 31.11,                  "Sweatshirt": 40.69, "Pullover Hoodie": 44.00, "Zip Hoodie": 45.57,                           "iPhone Cases": 24.75},
                } 
i=0

Productnumber = sum(len(products) for products in minPricelist.values())
total_price = round(sum(sum(prices.values()) for prices in minPricelist.values()),2)

Missingcount = 0
Desccount = 0
Expiringcount = 0
openit = True
Timeoutcounter = 0
Timeoutlist = []
Allstats = []
missingfive = 0
missingcolours = 0
for x in d:
   
    status = []
    message = defaultdict(list)
    message["Total"] = [float(0)]
    message["Totalsales"] = [0]
    tumblerreminder = "add Tumbler design"
    
    for y in Allitems:
        if x == y[0]:    
            if y[6] in deprecated_products:
                deprecated +=1
                continue
            if y[6] in deprecated_products:
                print("hello")
            if y[6] == "Tumbler":
                tumblerreminder = ""
                
            if y[2] == "US":            
                message["Title"] = y[1] + " Expiring in " + str(d[x].days) + " days"         #Title
                
                if y[10] not in Description and y[13] != "DELETED":                                                 #Description
                    message["Description"] = (["Incorrect Description", y[10]])
                    Desccount += 1


                if y[6] in ("Tank Top", "Raglan", "Standard T-Shirt", "Premium T-Shirt"):   # missing gender
                    if y[3] != "true":
                        message["Gender"].append(y[6] + " men's missing")
                    if y[4] != "true":
                        message["Gender"].append(y[6] + " women's missing")
                    
                if y[6] in ("Standard T-Shirt", "Premium T-Shirt"):
                    if y[5] != "true":
                        message["Gender"].append(y[6] + " kids' missing") 
                        

            message["Totalsales"] = [message["Totalsales"][0] + y[14]]
            message["Total"] = [message["Total"][0] + y[12]]

            if y[12] in minPricelist and y[12] < minPricelist[y[2]][y[6]]:                  # underpriced    
                        message["Underpriced"].append(y[6])
                        
            if y[12] in maxPricelist and y[12] < maxPricelist[y[2]][y[6]]:                  # overpriced    
                        message["Overpriced"].append(y[6])
            if y[6] not in color_counts:
                print (y[6])        
                                        
            required_colors = color_counts[y[6]]                                            # missing colour options
            if len(y[8]) < required_colors:
                message["Colours"].append(y[6] + " Colours missing: " + str(required_colors-len(y[8])))
                missingcolours+=1
 
            status.append(y[13])                                                            #Status counter

            if y[13] == "TIMED_OUT":
                message["TIMED_OUT"].append(y[6])
                Timeoutlist.append(y[1] + " " + y[2] + " " + y[6])

            if y[13] == "REJECTED":
                message["REJECTED"].append(y[6])
 
            if len (y[9])>1:
                if y[9][1] > y[9][0] and str(y[12])[-1] != "8":
                    message["Price"].append(y[6] + " " + y[2] + " - Adjust Price")                       # Adjust price
                    
            message["URL"] = y[11]
    
    if len(tumblerreminder)>0:
        message["Missing"].append(tumblerreminder)




    message["Status"] = str(len(status)) + " " + str(set(status))
    message["TIMED_OUT"] = set(message["TIMED_OUT"])
    message["Underpriced"] = set(message["Underpriced"])
    message["Overpriced"] = set(message["Overpriced"])
    message["Colours"] = set(message["Colours"])
    message["REJECTED"] = set(message["REJECTED"])
    message["Total"] = [round(message["Total"][0],2)]
    Target = total_price + message["Totalsales"][0]

    if float(message["Total"][0]) != Target:
        message["Not on Target"] = ["Not on Target"]
        
    message["Total"] = ["Total: ", message["Total"][0], "Target: ", Target]
    
    live = status.count("PUBLISHED") + status.count("PROPAGATED")
    

    if (live + status.count("PUBLISHING") + status.count("REVIEW") > 0):
        i+=1
        if i>499:
            print(message["Title"])
            print(message["Status"])

       
    
    if len(status) == status.count("REJECTED"):
        live += status.count("REJECTED")

        
    Hidelist = {'',}
       
    
    if (live > 0) and status.count("PUBLISHING") == 0 and status.count("REVIEW") == 0:
        message["Title"] = str(i) + " " + message["Title"]
        
        if d[x].days < 7:
            
            print (message["Title"])
            print(message["URL"])

        if (len(message["REJECTED"])==0):
            pop = message.pop("REJECTED", "pop")

        elif (0 < status.count("REJECTED") < len(status)):
            continue
        
        if (len(message["Underpriced"])==0):
            pop = message.pop("Underpriced", "pop")
        if (len(message["Overpriced"])==0):
            pop = message.pop("Overpriced", "pop")
        if (len(message["Colours"])==0):
            pop = message.pop("Colours", "pop")
        if (len(message["TIMED_OUT"])==0):
            pop = message.pop("TIMED_OUT", "pop")

            
        if live < Productnumber:
            Missing = Productnumber-live - status.count("TIMED_OUT") - status.count("TIMED_OUT_OK")
            if Missing > 0:
                Missingcount += Missing
                message["Missing"].append(Missing)
                
        pop = message.pop("Status", "pop")
              
        if len(set(message) - Hidelist) > 0 or ( i>490 and message["Totalsales"][0]>0) or i>497:
            print (message["Title"])

            webbrowser.get('brave').open(message["URL"])
            pop = message.pop("URL", "pop")
            
            for z in message:
                if z != "Title":
                    print("\t" + z)
                    for a in message[z]:
                        print("\t\t" +str(a))
                        
            if input("Press enter to continue...") != "":
                openit = False


print ("Total", i)
print ("Expiring", Expiringcount)
print ("Incorrect Description", Desccount)
print ("Missing", Missingcount, "=", int(Missingcount/150), "days")
print("Missing 6: ", missingfive)
print("Missing Colours: ", missingcolours)
print ("Timed out: ", len(Timeoutlist))
print ("Deprecated: ", deprecated)




