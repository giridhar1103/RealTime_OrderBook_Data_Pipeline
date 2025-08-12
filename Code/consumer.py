from cassandra.cluster import Cluster
from kafka import KafkaConsumer
from json import loads

# Initialize Kafka Consumer
try:
    consumer = KafkaConsumer(
        'orderbook_stream',
        bootstrap_servers=['<your_ec2_ip>'],
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )
except Exception as e:
    print("An error occurred while initializing the Kafka consumer:", e)
    consumer = None

# Initialize Cassandra Session
try:
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace("cryptoorderbook")
except Exception as e:
    print("An error occurred while initializing the Cassandra session or setting the keyspace:", e)
    session = None

# Process messages if Kafka consumer and Cassandra session are initialized
if consumer and session is not None:
    for message in consumer:
        if message.value:
            try:
                data = message.value
                session.execute('''
                    INSERT INTO orderbook (
                        ticker, system_time, midpoint, spread, buys, sells, 
                        bids_distance_0, bids_notional_0, bids_cancel_notional_0, 
                        bids_limit_notional_0, bids_market_notional_0, 
                        asks_distance_0, asks_notional_0, asks_cancel_notional_0, 
                        asks_limit_notional_0, asks_market_notional_0
                    ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
                    );
                ''', [
                    data.get('ticker'),
                    data.get('system_time'),
                    data.get('midpoint'),
                    data.get('spread'),
                    data.get('buys'),
                    data.get('sells'),
                    data.get('bids_distance_0'),
                    data.get('bids_notional_0'),
                    data.get('bids_cancel_notional_0'),
                    data.get('bids_limit_notional_0'),
                    data.get('bids_market_notional_0'),
                    data.get('asks_distance_0'),
                    data.get('asks_notional_0'),
                    data.get('asks_cancel_notional_0'),
                    data.get('asks_limit_notional_0'),
                    data.get('asks_market_notional_0')
                ])
            except Exception as e:

                print("An error occurred while processing or inserting data into Cassandra:", e)















