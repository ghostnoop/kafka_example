import os
import time

root = '/root/kafka/'

print('pkill java')
print('rm /root/...')

print(f"cd {root}kafka_2.13-2.7.0/ && bin/zookeeper-server-start.sh config/zookeeper.properties&")

print(f"cd {root}kafka_2.13-2.7.0/  && JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties&")

print(f"cd {root}CMAK/target/universal/cmak-3.0.0.5/ && bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080&")
