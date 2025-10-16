import csv


# with open('names.csv','r') as f:
#     file = csv.reader(f)

#     # next(file)  # it skip first value

#     with open('new.csv','w') as newf:
#         csvw = csv.writer(newf)

#         for line in file:
#             csvw.writerow(line)
        


with open('names.csv','r') as f:
    file = csv.DictReader(f)

    for line in file :
        print(line['Email'])
        with open('new.csv','w') as newf:
            fieldname = line.keys()
            csvw = csv.DictWriter(newf,fieldnames=fieldname)

            csvw.writeheader()

            for line in file:
                csvw.writerow(line)