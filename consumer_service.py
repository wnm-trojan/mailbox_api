"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-11
Email: warunanissanka44@gmail.com
Description: This component listens to messages from the Kafka topic (e.g., mailbox-messages) and saves them to the database (inbox store).
"""

import json
from confluent_kafka import Consumer, KafkaException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.message import Message
from app.kafka.topics import MESSAGE_TOPIC
from app.config import settings

# Kafka consumer setup
conf = {
    'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
    'group.id': 'mailbox-consumer-group',
    'auto.offset.reset': 'earliest',
}

consumer = Consumer(conf)
consumer.subscribe([MESSAGE_TOPIC])

def save_to_db(data: dict):
    db: Session = SessionLocal()
    try:
        message = Message(
            sender=data["sender"],
            receiver=data["receiver"],
            subject=data.get("subject"),
            body=data["body"]
        )
        db.add(message)
        db.commit()
        print(f"✅ Message saved from {data['sender']} to {data['receiver']}")
    except Exception as e:
        db.rollback()
        print(f"❌ DB error: {e}")
    finally:
        db.close()

print("📥 Kafka consumer running...")

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        try:
            message_data = json.loads(msg.value().decode("utf-8").replace("'", '"'))  # handle str(dict)
            save_to_db(message_data)
        except Exception as e:
            print(f"❌ Failed to process message: {e}")
except KeyboardInterrupt:
    print("⛔ Shutting down consumer...")
finally:
    consumer.close()
