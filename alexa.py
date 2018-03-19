import urllib, sys, re
for line in open("save2.csv"):
	csv_row = line.split()
	xml = urllib.urlopen('http://data.alexa.com/data?cli=10&dat=s&url=%s'%csv_row[1]).read()
	try: rank = int(re.search(r'<POPULARITY[^>]*TEXT="(\d+)"', xml).groups()[0])
	except: rank = -1
	print (rank,csv_row[1],csv_row[0])
