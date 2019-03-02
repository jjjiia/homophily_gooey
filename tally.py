##make dictionaries for all columns
import csv
import json
import collections
import operator
import json as simplejson

  
with open('400to500score.csv', 'Ub') as csvfile:
    spamreader = csv.reader(csvfile)
    
    #for nycZip in nycZips_geo:
    csvfile.seek(0)
    
    dots = []
    
    for row in spamreader:
        header = row
        print header
        break
        
    for row in spamreader:
        entry = {}
        for i in range(len(row)):
            #print header[i], row[i]
            entry[header[i]]=row[i]
        dots.append(entry)
    
    with open("400to500score.json","w") as outfile:
        json.dump(dots,outfile)
            
        
        #outfile.write(simplejson.dumps(simplejson.loads(dots), indent=4, sort_keys=True))
        

