import os
from xml.dom import minidom
from datetime import datetime


def read_all_files(path, inputPath, outputPath):
    date_time = str(str(datetime.now()).replace(":","_"))
    output_file = outputPath + "Schema_Validation_" + date_time + ".txt"
    file_write = open(output_file, "w+")
    file_write.seek(0)
    for file in os.listdir(path):
        inputfile = inputPath + file
        file_read = open(inputfile, "r", encoding="utf8")
        mydoc = minidom.parse(file_read)
        storeID = mydoc.getElementsByTagName('storeID')
        transactionDate = mydoc.getElementsByTagName('transactionDate')
        registerID = mydoc.getElementsByTagName('registerID')
        transactionNumber = mydoc.getElementsByTagName('transactionNumber')
        values = [storeID, transactionDate, registerID, transactionNumber]
        for v in values:
            file_write.write(v[0].firstChild.data + " ")
        file_write.write("\n")
    file_write.close()


path = os.getcwd() + "\Input"  # os.getcwd() gets the current working directory
inputPath, outputPath = "./Input/", "./Output/"
read_all_files(path, inputPath, outputPath)
