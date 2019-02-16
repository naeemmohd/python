# import os module
import os

# check if the directory exits or not
dirPath = 'logs';
# create directory only if it does not exist
if not os.path.exists(dirPath):
    os.mkdir(dirPath)

# create/open file in write(w), read(r) or append(a) mode, '+' means if not exist then create
filePath = dirPath + '/salary20190201.dat';
if not os.path.isfile(filePath):
    theFile = open(filePath,'w+')
    theFile.write('InvoiceID,CustomerName,Balance,IsProcessed\n')
    theFile.write('1,Kelly Bennett,551,0\n')
    theFile.write('2,Mary Wilson,709,0\n')
    theFile.write('3,Linda Lynch,648,0\n')
    theFile.close()

# open file in read mode and loop through the lines
theFile = open(filePath,'r')
for line in theFile:
    print(line)
theFile.close()