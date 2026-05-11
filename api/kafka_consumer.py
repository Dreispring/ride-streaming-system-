from kafka import KafkaConsumer
import json
import time

while True:
    try:
        consumer = KafkaConsumer(
            "ride-events",
            bootstrap_servers="kafka:9092",
            auto_offset_reset="latest",
            group_id="ride-consumer-group",
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )

        print("✅ Connected to Kafka")
        break

    except Exception as e:
        print(f"⏳ Waiting for Kafka... {e}")
        time.sleep(5)

print("🚀 Waiting for messages...")

for message in consumer:
    print("📩 Received event:")
    print(message.value)
