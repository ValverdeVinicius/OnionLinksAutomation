import requests
import random
import re

def scrape(newData):
	yourQuery = newData
	
	if " " in yourQuery:
		yourQuery = yourQuery.replace(" ", "+")
		
	url = "https://ahmia.fi/search/?g={}".format(yourQuery)
	request = requests.get(url)
	content = request.text
	regexQuery = "\w+\.onion"
	mineData = re.findall(regexQuery, content)
	
	n = random.randint(1, 9999)
	
	fileName = "sites{}.txt".format(str(n))
	print("Saving to... ", fileName)
	mineData = list(dict.fromkeys(mineData))
	
	for k in mineData:
		with open(fileName, "a") as newFile:
			k = k + "\n"
			newFile.write(k)
			
	print("All the files written to a text file: ", fileName)
	
	with open(fileName) as input_file:
		head = [next(input_file) for x in range(5)]
		contents = '\n'.join(map(str, head))
		print(contents)
	
	
newData = input("[*]Enter your Query:")
scrape(newData)
