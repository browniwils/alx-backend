import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (err) => {
  const message = 'Redis client not connected to the server:';
  console.log(message, err.toString());
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  console.log(await promisify(client.GET).bind(client)(schoolName));
};

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
  const message = 'Redis client connected to the server';
  console.log(message);
  await main();
});
