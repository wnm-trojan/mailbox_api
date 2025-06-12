"""
Author: WarunaNissanka
Project: Mailbox API
Created: 2025-06-12 
Email: warunanissanka44@gmail.com
Description: 
"""

from confluent_kafka import Producer
from app.config import settings

producer = Producer({'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def send_message_to_kafka(topic: str, message: dict):
    producer.produce(topic, value=str(message), callback=delivery_report)
    producer.flush()
