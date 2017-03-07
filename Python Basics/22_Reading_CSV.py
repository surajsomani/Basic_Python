import csv
#library to handle csv files
with open('example.csv') as csvfile: #naming the file as csvfile
    readCSV = csv.reader(csvfile, delimiter=',') #reading the file
    for row in readCSV: #reading each row
        print(row) #print all columns in 1st row
        print(row[0]) #print 1st column Here also index starts with 0
        print(row[0],row[1],row[2],) #print 1st, 2nd and 3rd column

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        dates.append(date)
        colors.append(color)
    print(dates)
    print(colors)

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        dates.append(date)
        colors.append(color)
    print(dates)
    print(colors)
    # now, remember our lists?
    whatColor = input('What color do you wish to know the date of?:')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of',whatColor,'is:',theDate)
#if you enter something that doesn't exist, you will get an ugly error.
