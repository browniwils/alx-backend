import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  const message = 'Redis client not connected to the server:';
  console.log(message, err.toString());
});

const publishMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
};

client.on('connect', () => {
  const message = 'Redis client connected to the server';
  console.log(message);
});

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
