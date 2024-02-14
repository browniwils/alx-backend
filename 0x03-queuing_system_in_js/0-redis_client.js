import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  const message = 'Redis client not connected to the server:';
  console.log(message, err.toString());
});

client.on('connect', () => {
  const message = 'Redis client not connected to the server:';
  console.log(message);
});
