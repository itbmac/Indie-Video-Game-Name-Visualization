#!/usr/bin/env python

import csv
import json
import urllib

url = "http://www.kimonolabs.com/api/657km6c2?apikey=e2149333a4ca179bc0d26fe05ee93562";
f = csv.writer(open("test.csv", "wb+"))
fstr = open('test.txt', 'r+')
fstrRating = open('testRating.txt', 'r+')

s = ""
r = ""
numWords = 0
numRatings = 0

for x in xrange(1, 39):
    results = json.load(urllib.urlopen("http://www.kimonolabs.com/api/657km6c2?apikey=e2149333a4ca179bc0d26fe05ee93562"+"&page="+str(x)))
    j = results
    j = j["results"]["collection1"]
    
    for j in j:
        l = (j["game_name"]["text"].encode('ascii', 'ignore')).split(" ")
        numWords += len(l);
        for i in xrange(0, len(l)):
            numRatings += 1;
            f.writerow([l[i],
                    j["game_score"].encode('ascii', 'ignore')])
            s += " , " + l[i]
            r += " , " + str(j["game_score"].encode('ascii', 'ignore'))
fstr.write(s)
fstrRating.write(r)
print (numWords, numRatings)