import csv
from datetime import datetime 

relevanteStatussen = ["Geplaatst", "Verwijderd", "Opdracht uitvoeren"]
outputFile = []
vorigeDatum = ""
vorigeElement = ""

with open('BordLog.csv', 'rb') as f:
    reader = csv.reader(f)

    for row in reader:
    	logRows = row[3].split("\n")
    	for logRow in logRows:
    		logElement = logRow.split("\t")
    		try:
    			if logElement[3] == "Status" and logElement[6] in relevanteStatussen:
    				if logElement[0] != vorigeDatum or vorigeElement != row[0]:
						datum = datetime.strptime(logElement[0], '%d-%m-%Y')
						outputRow = [row[0], row[1], datum, logElement[2], logElement[3], logElement[6]]
						outputFile.append(outputRow)
						vorigeDatum = logElement[0]
						vorigeElement = row[0]
    		except Exception as e:
    			pass

with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(outputFile)
