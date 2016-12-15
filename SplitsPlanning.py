import csv
from datetime import datetime 

outputFile = []

with open('planning.csv', 'rb') as f:
    reader = csv.reader(f)

    for row in reader:
    	logRows = row[4].split("+")
    	for logRow in logRows:
    		logElement = logRow.strip()
    		try:
    			# datum = datetime.strptime(logElement[0], '%d-%m-%Y')
				outputRow = [row[0], row[1], row[2], row[3], logElement, row[5], row[6]]
				outputFile.append(outputRow)
    		except Exception as e:
    			pass

with open("outputPlanning.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(outputFile)
