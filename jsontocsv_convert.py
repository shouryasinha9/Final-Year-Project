# Python program to convert
# JSON file to CSV


import json
import csv

import csv2xlsx


def json2csv(filename):
    try:
        with open(filename) as json_file:
            data = json.load(json_file)

        employee_data = data['details']

        # now we will open a file for writing
        data_file = open('Save_Data_GovtID.csv', 'w')

        # create the csv writer object
        csv_writer = csv.writer(data_file)

        # Counter variable used for writing
        # headers to the CSV file
        count = 0

        for emp in employee_data:
            if count == 0:
                # Writing headers of CSV file
                header = emp.keys()
                csv_writer.writerow(header)
                count += 1

            # Writing data of CSV file
            csv_writer.writerow(emp.values())

        data_file.close()

        csv2xlsx.csvToxlsx('D:\Final-Year-Project\\Save_Data_GovtID.csv')
        return 1
    except Exception as ex:
        return 0
