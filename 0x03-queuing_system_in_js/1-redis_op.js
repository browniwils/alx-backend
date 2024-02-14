import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  const message = 'Redis client not connected to the server:';
  console.log(message, err.toString());
});

client.on('connect', () => {
  const message = 'Redis client connected to the server:';
  console.log(message);
});

const setNewSchool = (schoolName, value) => {
  client.SET(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.GET(schoolName, (_, reply) => {
    console.log(reply);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
