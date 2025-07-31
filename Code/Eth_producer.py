from kafka import KafkaProducer
from time import sleep
from json import dumps
import pandas as pd

dataframe = pd.read_csv('ETH-1sec_Tf.csv')

KAFKA_TOPIC = 'orderbook_stream' # Kafka topic name

try:
    producer = KafkaProducer(
        bootstrap_servers=['<your_ec2_ip_addres>'],
        value_serializer=lambda x: dumps(x).encode('utf-8')
    )

except Exception as e:
    print("An error occurred while initializing the producer or reading the CSV file:", e)
    producer = None
    dataframe = None

if producer and dataframe is not None:
    try:
        for _, row in dataframe.iterrows():
            data = row.to_dict()
            producer.send(KAFKA_TOPIC, value=data)
            sleep(1)
    
    except KeyboardInterrupt:
             print("\nProcess interrupted! Exiting...")

    except Exception as e: 
              print("An error occurred while sending data to Kafka:", e) 

    finally:
         
         try: 
             producer.flush() 
             producer.close() 
             print("Kafka producer closed.") 
         except Exception as e: 
             print("An error occurred while flushing or closing the producer:", e)
