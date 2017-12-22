import csv
import uuid

ff = open('after1.csv', 'w')
wr = csv.writer(ff)
with open('after.csv', 'r') as f:

    rdr = csv.reader(f)
    next(rdr, None)
    counter = 0
    iid = uuid.uuid4()
    for line in rdr:
        line.insert(0, iid)
        wr.writerow(line)
        counter = counter + 1
        print(counter)
ff.close
