from cassandra.cluster import Cluster

try:
    # Connect to Cassandra
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    # Set keyspace
    session.set_keyspace("cryptoorderbook")

    # Truncate the table
    session.execute("TRUNCATE orderbook;")

    print("Table 'orderbook' has been cleared successfully.")

except Exception as e:
    print("An error occurred while truncating the table:", e)
