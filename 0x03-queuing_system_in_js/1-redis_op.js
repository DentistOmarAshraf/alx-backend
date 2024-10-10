import { createClient } from 'redis';
import redis from 'redis';

const client = createClient()

client.on('connect', () => {
    console.log('Redis client connected to the server');
})

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error.message}`);
})

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value,  redis.print)
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, redis.print);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');