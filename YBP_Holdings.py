from isbnlib import *
import easygui as eg
import sys
import csv
import os

# clean-up old files
os.system("del YBP_HOLDINGS.txt")

# select file
csv_file_path = eg.fileopenbox(msg='Select .CSV file', 
                            title='Select File',
                            filetypes='*.csv')
                            
if csv_file_path == None:
    print("No file selected.")
    sys.exit()

# open input and output files   
csv_file = open(csv_file_path, "r")
output_file = open("YBP_HOLDINGS.txt", "w")

# initiate csv object and parse
csv_object = csv.reader(csv_file, delimiter=';')
for row in csv_object:
    for isbn in row:
        isbn = isbn.replace(" ", "")
        bad_isbn = notisbn(isbn, level='strict')
        if bad_isbn == True: # Invalid ISBN
            continue
        if bad_isbn == False: # Valid ISBN
            isbn = to_isbn13(isbn)
            output_file.write(f"{isbn}\n")
            break
            
# finish
eg.msgbox("Done.", "Finished")