from time import sleep
from kafka import KafkaProducer
from faker import Faker
import random, string, datetime
import json

fake = Faker()
producer = KafkaProducer(bootstrap_servers=['kafka-1:19092'])


def __id_generator__(size=20, chars=string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def generate_random_post_function():
    post = {
        "id": __id_generator__(size=20),
        "sender_id": random.randint(1, 1000000),
        "text": fake.sentence(),  # Use Faker to generate a random sentence
        "created_at": int(datetime.datetime.now().timestamp()),
        "like_count": random.randint(0, 10),
        "user": {
            "id": random.randint(1, 1000000),
            "username": fake.user_name(),  # Use Faker to generate a random username
            "follower_count": random.randint(0, 500),
        }
    }
    return post


for _ in range(500):
    data = generate_random_post_function()
    print(data)

    # Serialize the data dictionary to JSON and encode it to bytes before sending to Kafka
    data_bytes = json.dumps(data).encode('utf-8')

    producer.send('dataak', value=data_bytes)
    sleep(3)
