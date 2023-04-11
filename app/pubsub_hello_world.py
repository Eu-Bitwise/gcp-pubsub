import os
import json
import logging
from google.cloud import pubsub_v1

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Load configuration from JSON file
with open("../config.json") as f:
    config = json.load(f)
    
# Set the environment variable for the Google Cloud JSON key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "my-sandbox-383402-c0339066a0d2.json"

project_id = config["project_id"]
topic_id = config["topic_id"]
subscription_id = config["subscription_id"]

# Create a Publisher client
logging.info("Creating Publisher client...")
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Create a Subscriber client
logging.info("Creating Subscriber client...")
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

# Create a topic
logging.info(f"Creating topic {topic_id}...")
publisher.create_topic(request={"name": topic_path})

# Create a subscription
logging.info(f"Creating subscription {subscription_id}...")
subscriber.create_subscription(request={"name": subscription_path, "topic": topic_path})

# Publish a message
message = "Hello, World!"
data = message.encode("utf-8")
logging.info(f"Publishing message: {message}")
publisher.publish(topic_path, data)

# Callback function to process the received message
def callback(message):
    received_message = message.data.decode("utf-8")
    logging.info(f"Received message: {received_message}")
    message.ack()

    # Stop listening for more messages
    future.cancel()

    logging.info(f"Success!")
    
# Subscribe to the topic and process messages
logging.info("Subscribing to messages...")
future = subscriber.subscribe(subscription_path, callback=callback)

# Wait to receive the message and subscription to be canceled
try:
   future.result()
except Exception as e:
    print("An error occurred: {}".format(e))
    
logging.info("Exiting program.")
