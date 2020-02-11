import csv
from pprint import pprint
from matplotlib import pyplot


# csv data source
filename = 'FL_insurance_sample.csv'

# opening csv data source
with open(filename) as csv_file:

    # all csv data
    reader = csv.reader(csv_file)

    # header titles
    header_row = next(reader)
    pprint(header_row)
    print('\n')

    # fetching header titles with indexes
    print('All Header Titles:')
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # accessing particular column  of data
    policyID = []

    # accessing all data from a row
    for row in reader:
        policyID.append(int(row[0]))

    print('\npolicyID:')
    print(policyID)

    # plotting data
    figure = pyplot.figure(dpi=128, figsize=(10, 6)) # width=10in, height=6in
    pyplot.plot(policyID, c='red')

    # format plot
    pyplot.title('Title', fontsize=16)
    pyplot.xlabel('x-label', fontsize=16)
    pyplot.ylabel('y-label', fontsize=16)
    pyplot.tick_params(axis='both', which='both', labelsize=10, color='red')
    pyplot.show()






