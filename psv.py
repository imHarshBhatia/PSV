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

# print(datetime.now())
# mydoc = minidom.parse('log.xml')
# storeID = mydoc.getElementsByTagName('storeID')
# transactionDate = mydoc.getElementsByTagName('transactionDate')
# registerID = mydoc.getElementsByTagName('registerID')
# transactionNumber = mydoc.getElementsByTagName('transactionNumber')
# values = [storeID, transactionDate, registerID, transactionNumber]
# for v in values:
#     print(v[0].firstChild.data, end="")
# print()
# print(storeID[0].firstChild.data,end="")
# print(items[0].firstChild.key)
# print('Store Number: ', end = "")
# print(items[0].childNodes[0].POSLogDocument)

# mydoc = minidom.parse('items.xml')
#
# items = mydoc.getElementsByTagName('item')
#
# # one specific item attribute
# print('Item #2 attribute:')
# print(items[1].attributes['name'].value)
#
# # all item attributes
# print('\nAll attributes:')
# for elem in items:
#     print(elem.attributes['name'].value)
#
# # one specific item's data
# print('\nItem #2 data:')
# print(items[1].firstChild.data)
# print(items[1].childNodes[0].data)
#
# # all items data
# print('\nAll item data:')
# for elem in items:
#     print(elem.firstChild.data)
