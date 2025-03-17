from kafka import KafkaProducer
from time import sleep
from json import dumps
import pandas as pd
import multiprocessing

KAFKA_TOPIC = 'crypto_stream'

btc_df = pd.read_csv('BTC_1sec_Tf.csv')
eth_df = pd.read_csv('ETH_1sec_Tf.csv')
ada_df = pd.read_csv('ADA_1sec_Tf.csv')

def send_data(dataframe, symbol, producer):
    for _, row in dataframe.iterrows():
        data = row.to_dict()
        data['symbol'] = symbol
        producer.send(KAFKA_TOPIC, value=data)
        sleep(1)

if __name__ == "__main__":
    try:
        producer = KafkaProducer(
            bootstrap_servers=['54.176.118.167:9092'],
            value_serializer=lambda x: dumps(x).encode('utf-8')
        )

        btc_process = multiprocessing.Process(target=send_data, args=(btc_df, 'BTC', producer))
        eth_process = multiprocessing.Process(target=send_data, args=(eth_df, 'ETH', producer))
        ada_process = multiprocessing.Process(target=send_data, args=(ada_df, 'ADA', producer))

        btc_process.start()
        eth_process.start()
        ada_process.start()

        btc_process.join()
        eth_process.join()
        ada_process.join()

        producer.close()
        print("Kafka producer closed.")

    except Exception as e:
        print("Error:", e)
