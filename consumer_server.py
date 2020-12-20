from kafka import KafkaConsumer

consumer = KafkaConsumer(boorstrap_server='localhost:9092',
                        auto_offset_reset='earliest',
                        consumer_timeout_ms=1000)

print ('set consumer')

consumer.subscribe(['department.call.service.log'])

print ('set subscribe')

for message in consumer:
    print(message.value)