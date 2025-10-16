from cassandra.cluster import Cluster

try:
    # Connect to Cassandra
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    # Set keyspace (Assuming 'CryptoOrderbook' is manually created)
    session.set_keyspace("cryptoorderbook")

    # Create table
    session.execute('''
        CREATE TABLE IF NOT EXISTS orderbook (
            ticker varchar,
            system_time timestamp,
            midpoint float,
            spread float,
            buys float,
            sells float,
            bids_distance_0 float,
            bids_notional_0 float,
            bids_cancel_notional_0 float,
            bids_limit_notional_0 float,
            bids_market_notional_0 float,
            asks_distance_0 float,
            asks_notional_0 float,
            asks_cancel_notional_0 float,
            asks_limit_notional_0 float,
            asks_market_notional_0 float,
            PRIMARY KEY (ticker, system_time)
        );
    ''')

    print("Table 'orderbook' created successfully in keyspace 'CryptoOrderbook'.")

except Exception as e:
    print("An error occurred while creating the table:", e)
