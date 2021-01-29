import csv

namesToRemove = []
csvFilePath = "~/namesToBeDisqualified.csv"   #path to the csv file containing the names
def generateNamesFromCsvFile():
    with open(csvFilePath, mode = 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            line_count = 0
            first = 1
            for row in csv_reader:
                if first: #discard column name
                    first = 0
                    continue
                print(row)
                namesToRemove.append(row[0])
    return namesToRemove