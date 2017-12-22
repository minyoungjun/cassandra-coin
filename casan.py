from cassandra.cluster import Cluster
import csv
import time

cluster = Cluster()
session = cluster.connect()

#session.execute(
#        """
#        CREATE KEYSPACE py_casandra
#            WITH REPLICATION = {
#                'class' : 'NetworkTopologyStrategy',
#                'datacenter1' : 1
#            };
#        """
#        )

session.execute('USE py_casandra')

session.execute('DROP TABLE py_casandra.coins')

start_time = time.time()

session.execute(
        """
        CREATE TABLE IF NOT EXISTS py_casandra.coins (
            time timestamp PRIMARY KEY,
            open float,
            high float,
            low float,
            close float,
            vol_btc double,
            vol_currency double,
            weighted double);
        """
        )

with open('bitstampUSD_1-min_data_2012-01-01_to_2017-10-20.csv', 'r') as f:

    rdr = csv.reader(f)
    next(rdr, None)
    counter = 0
    for line in rdr:
        if (counter < 50000):
            session.execute(
                    """
                    INSERT INTO py_casandra.coins(time, open, high, low, close, vol_btc, vol_currency, weighted)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    IF NOT EXISTS;
                    """,(line[0] + '000', float(line[1]), float(line[2]), float(line[3]), float(line[4]), float(line[5]), float(line[6]), float(line[7]))
                    )
        counter = counter + 1
        print(counter)


rows = session.execute('SELECT time, close, vol_btc FROM coins LIMIT 50000')

for row in rows:
    print row.time, row.close, row.vol_btc

print("--- %s seconds ---" %(time.time() - start_time))

