# GCP PubSub Messaging Flow

This project demonstrates the basic usage of Google Cloud Pub/Sub with a simple publish and subscribe usage. It consists of a Python script to create a topic and subscription, an express server that listens for messages, and another Python script to publish messages to the topic. The messages are displayed in a browser window using Socket.IO.

## Requirements
- Python 3.6+
- Node.js 12+
- Google Cloud SDK
- Google Cloud account with a configured project and Pub/Sub API enabled
- Google Cloud service account with Pub/Sub Editor role and JSON key downloaded from the Google Cloud Console.

## Setup

1. Install the required Python packages:
`pip install google-cloud-pubsub google-auth google-auth-transport-requests`

2. Install the required Node.js packages:
`npm install`

3. Update the config.json file with your Google Cloud project information and the path to your service account key JSON file.

## Usage 

1. Run the pubsub_hello_world.py script to create a topic and subscription in your Google Cloud project:
`python pubsub_hello_world.py`

2. Start the server by running the following command in the app directory:
`node server.js`
(The server will start on port 3000 by default and open a browser window displaying the received messages.)

3. Run the publisher.py script to publish a message to the topic: 
`python publisher.py`

4. Observe the received message in the browser window.
