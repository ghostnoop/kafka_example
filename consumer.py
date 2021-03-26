from kafka import KafkaConsumer
import json

if __name__ == '__main__':
    consumer = KafkaConsumer(
        'java',
        bootstrap_servers=['ip:9092'],
        auto_offset_reset='earliest',
        group_id='consumer-group-B'
    )
    print('starting the consumer')
    for msg in consumer:
        print('msg', json.loads(msg.value))
