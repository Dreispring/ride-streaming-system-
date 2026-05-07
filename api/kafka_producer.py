from kafka import KafkaProducer
import json
import os
import time

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

producer = None


def get_producer():
    global producer

    if producer is None:
        for _ in range(10):
            try:
                producer = KafkaProducer(
                    bootstrap_servers=KAFKA_BROKER,
                    value_serializer=lambda v: json.dumps(v).encode("utf-8")
                )
                print("✅ Connected to Kafka")
                return producer
            except Exception as e:
                print(f"⏳ Waiting for Kafka... {e}")
                time.sleep(3)

        raise Exception("❌ Cannot connect to Kafka")

    return producer


def send_trip_event(event: dict):
    try:
        producer = get_producer()

        future = producer.send("ride-events", event)
        result = future.get(timeout=10)  # đảm bảo gửi thành công

        print(f"📤 Sent event to Kafka: {event}")
        print(f"📍 Topic: {result.topic}, Partition: {result.partition}")

    except Exception as e:
        print(f"❌ Failed to send event: {e}")
