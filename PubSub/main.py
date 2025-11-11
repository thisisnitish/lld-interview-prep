# https://github.com/ashishps1/awesome-low-level-design/tree/main/solutions/python/pubsubsystem

"""
We will just make it simple:
3 components:
1. Publisher
2. Subscriber
3. Topics

Entities:
Message, Topic, Publisher, Subscriber, PubSub, Controller
"""

from pubsub import PubSub
from publisher import Publisher
from subscriber import Subscriber
from concretesubscriber import Subscriber1
from models.topic import Topic
from models.message import Message

def run():
    pubsubSystem = PubSub()

    # create topics
    pubsubSystem.create_topic("Topic1")
    pubsubSystem.create_topic("Topic2")

    # create subscribers
    subscriber1 = Subscriber1("Subscriber1")
    subscriber2 = Subscriber1("Subscriber2")
    subscriber3 = Subscriber1("Subscriber3")

    # subscribe to the topic
    pubsubSystem.subscribe("Topic1", subscriber1)
    pubsubSystem.subscribe("Topic1", subscriber2)
    pubsubSystem.subscribe("Topic2", subscriber2)
    pubsubSystem.subscribe("Topic2", subscriber3)

    # create publishers
    publisher1 = Publisher(pubsubSystem.get_topics().get("Topic1"))
    publisher2 = Publisher(pubsubSystem.get_topics().get("Topic2"))

    msg1 = Message("Message1 for Topic1")
    msg2 = Message("Message2 for Topic1")
    msg3 = Message("Message1 for Topic2")

    # Publish messages
    publisher1.publish(message=msg1)
    publisher1.publish(message=msg2)
    publisher2.publish(message=msg3)


if __name__ == '__main__':
    run()
