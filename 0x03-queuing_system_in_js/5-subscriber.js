import { createClient } from 'redis';

const EXIT_SERVER_MSG = 'KILL_SERVER';
const client = createClient();

client.on('error', (err) => {
  const message = 'Redis client not connected to the server:';
  console.log(message, err.toString());
});

client.on('connect', () => {
  const message = 'Redis client connected to the server';
  console.log(message);
});

client.subscribe('holberton school channel');
client.on('message', (_, msg) => {
  console.log(msg);
  if (msg === EXIT_SERVER_MSG) {
    client.unsubscribe();
    client.quit();
  }
});
