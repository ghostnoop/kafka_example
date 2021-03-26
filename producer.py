import time

from kafka import KafkaProducer
import json

from data import get_test_user


def json_serializer(data):
    return json.dumps(data).encode('utf-8')


producer = KafkaProducer(bootstrap_servers=['ip:9092'],
                         value_serializer=json_serializer, )

if __name__ == '__main__':
    while True:
        test_user = get_test_user()
        print(test_user)
        producer.send('java', test_user)

        time.sleep(4)
