from cassandra.cluster import Cluster
import csv
import time

cluster = Cluster()

session = cluster.connect()

session.execute('USE py_casandra')
#session.execute('DROP  TABLE coins;')
#session.execute('DROP TABLE py_casandra.coins')
start_time = time.time()

session.execute(
        """
        CREATE TABLE IF NOT EXISTS py_casandra.coins (
            id uuid,
            time timestamp,
            open float,
            high float,
            low float,
            close float,
            vol_btc float,
            vol_currency float,
            weighted float,
            PRIMARY KEY(id, time)
        ) WITH CLUSTERING ORDER BY (time DESC);
        """
        )






"""
ff = open('after.csv', 'w')
wr = csv.writer(ff)
with open('bitstampUSD_1-min_data_2012-01-01_to_2017-10-20.csv', 'r') as f:

    rdr = csv.reader(f)
    next(rdr, None)
    counter = 0
    for line in rdr:
        line[0] = line[0] + '000'
        wr.writerow(line)
        counter = counter + 1
        print(counter)
ff.close
"""
