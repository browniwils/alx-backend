import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  const message = 'Redis client not connected to the server:';
  console.log(message, err.toString());
});

const updateHash = (hashName, fieldName, fieldValue) => {
  client.HSET(hashName, fieldName, fieldValue, print);
};

const printHash = (hashName) => {
  client.HGETALL(hashName, (_, reply) => console.log(reply));
};

const main = () => {
  const places = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [key, value] of Object.entries(places)) {
    updateHash('HolbertonSchools', key, value);
  }
  printHash('HolbertonSchools');
}

client.on('connect', () => {
  const message = 'Redis client connected to the server';
  console.log(message);
  main();
});
