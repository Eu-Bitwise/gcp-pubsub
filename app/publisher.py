import json
import requests
import base64
import logging
import os
from google.oauth2 import service_account
import google.auth.transport.requests

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Load configuration from JSON file
with open("../config.json") as f:
    config = json.load(f)

project_id = config["project_id"]
topic_id = config["topic_id"]
key_file_path = config["key_file_path"]

# Set the environment variable for the Google Cloud JSON key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path

# Create the topic path
topic_path = f"projects/{project_id}/topics/{topic_id}"

# Publish a message using the Google Cloud Pub/Sub REST API
message = "Hello, World!"
data = base64.b64encode(message.encode("utf-8")).decode("utf-8")
logging.info(f"Publishing message: {message}")

url = f"https://pubsub.googleapis.com/v1/{topic_path}:publish"

# Use the Service Account key to create credentials and get an access token
credentials = service_account.Credentials.from_service_account_file(
    key_file_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

request = google.auth.transport.requests.Request()
credentials.refresh(request)
access_token = credentials.token

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
}

payload = {
    "messages": [
        {
            "data": data,
        }
    ],
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    logging.info("Message published successfully.")
else:
    logging.error(f"Failed to publish message. Response: {response.text}")
