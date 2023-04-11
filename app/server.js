const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const { PubSub } = require('@google-cloud/pubsub');
const fs = require('fs');
const opn = require('opn');  // Import the opn package

// Set up Express server
const app = express();
const server = http.createServer(app);
const io = socketIO(server);

// Serve the static files
app.use(express.static('public'));

// Load configuration from JSON file
const config = JSON.parse(fs.readFileSync('../config.json'));

// Set up Google Cloud Pub/Sub
const pubsub = new PubSub({
    keyFilename: config.key_file_path,
});

const subscription = pubsub.subscription(config.subscription_id);

// Subscribe to the topic and process messages
subscription.on('message', (message) => {
    const receivedMessage = message.data.toString('utf-8');
    console.log(`Received message: ${receivedMessage}`);
    io.emit('pubsub-message', receivedMessage);
    message.ack();
});

// Start the server
const port = process.env.PORT || 3000;
server.listen(port, () => {
    console.log(`Server running on port ${port}`);

    // Open a browser window
    console.log(`Opening new windows on browser`);
    opn(`http://localhost:${port}`);
});
