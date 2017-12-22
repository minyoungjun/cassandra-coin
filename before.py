import csv
import uuid
import datetime

ff = open('after3.csv', 'w')
wr = csv.writer(ff)
with open('bitstampUSD_1-min_data_2012-01-01_to_2017-10-20.csv', 'r') as f:

    rdr = csv.reader(f)
    next(rdr, None)
    counter = 1
    for line in rdr:
        line[0] = datetime.datetime.fromtimestamp(int(line[0])).strftime('%Y-%m-%d %H:%M:%S')
        line.insert(0, counter)
        wr.writerow(line)
        counter = counter + 1
        print(counter)
ff.close
