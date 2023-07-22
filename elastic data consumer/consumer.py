from kafka import KafkaConsumer
from elasticsearch import Elasticsearch
from protobuf3.message import Message
from protobuf3.fields import StringField, Int32Field, MessageField

# Kafka Consumer
consumer = KafkaConsumer(
    'dataak',
    bootstrap_servers=['kafka-2:29092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='dataak_group')


# Protobuf schema
class User(Message):
    id = Int32Field(field_number=1, required=True)
    username = StringField(field_number=2, required=True)
    follower_count = Int32Field(field_number=3, required=True)


class Transaction(Message):
    id = StringField(field_number=1, required=True)
    sender_id = Int32Field(field_number=2, required=True)
    text = StringField(field_number=3, required=True)
    created_at = Int32Field(field_number=4, required=True)
    like_count = Int32Field(field_number=5, required=True)
    user = MessageField(field_number=6, message_cls=User)


# Elasticsearch
es = Elasticsearch(HOST='http://elasticsearch',PORT=9200)
# http_auth=('user', 'secret'),
#   scheme="http",
#  port=9200,)
# ssl_context=context,)  # Include the 'http' scheme for localhost


# Kafka listener
for message in consumer:
    message = message.value
    details = Transaction()
    details.parse_from_bytes(message)

    # Prepare data for Elasticsearch
    data = {
        "id": details.id,
        "sender_id": details.sender_id,
        "text": details.text,
        "created_at": details.created_at,
        "like_count": details.like_count,
        "user": {
            "id": details.user.id,
            "username": details.user.username,
            "follower_count": details.user.follower_count
        }
    }

    # Index data into Elasticsearch
    res = es.index(index='your_index_name', body=data)  # Replace 'your_index_name' with the desired index name
    print("Data indexed successfully:", res)
