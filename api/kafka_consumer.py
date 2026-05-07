from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'ride-events',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🚀 Consumer started...")

for message in consumer:
    print("Received event:", message.value)
