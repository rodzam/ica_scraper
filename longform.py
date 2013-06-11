##############################################################
# Program name: ICA Conference Site Scraper (Long Form Data Converter)
# Version: 0.1-alpha
# By: Rodrigo Zamith
# License: MPL 2.0 (see LICENSE file in root folder)
# Additional thanks: 
##############################################################

import csv
import ast

# Set data file for processing
data_file = "data.csv"

# Open CSV Output File
output_file = open("data-author-long.csv", "wb")
output_file_wr = csv.writer(output_file, quoting=csv.QUOTE_ALL)

# Create lists to populate
caselist = []

# Transfer CSV rows into a list
print "Opening data file..."
with open(data_file, 'rb') as data_file:
    reader = csv.reader(data_file)
    for row in reader:
        caselist.append(row)

# Transform data into long form
header = ["item_id", "case_id", "case_title", "case_author", "case_institution", "author_order", "case_session", "case_unit", "case_type", "case_area", "case_time", "case_place"]
output_file_wr.writerow(header)
listpos = 0
item_id = 1
listlength = len(caselist[1:])
for case in caselist[1:]:
    print "Processing item %s of %s (%s%% complete)" % (listpos + 1, listlength, round(100*float(listpos)/float(listlength), 2))
    case_id = case[0]
    case_title = case[1]
    case_authorlist = ast.literal_eval(case[2])
    case_session = case[3]
    case_unit = case[4]
    case_type = case[5]
    case_area = case[6]
    case_time = case[7]
    case_place = case[8]
    author_order = 0
    
    for item in case_authorlist:
        author_order += 1
        try:
            case_author = str(item).split(", ", 1)[0]
        except:
            case_author = "None"
        try:
            case_institution = str(item).split(", ", 1)[1]
        except:
            case_institution = "None"
        line = [item_id, case_id, case_title, case_author, case_institution, author_order, case_session, case_unit, case_type, case_area, case_time, case_place]
        output_file_wr.writerow(line)
        item_id += 1
    listpos += 1
print "Finished!"
